import nltk
import numpy as np
from sentence_transformers import SentenceTransformer, util
from pydub import AudioSegment

from .sentiment import get_sentiment
from .keywords import extract_keywords
from .summarizer import summarize_segment

model = SentenceTransformer("all-MiniLM-L6-v2")

def format_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{int(m):02d}:{int(s):02d}"

def embedding_segmentation(text):
    sentences = nltk.sent_tokenize(text)

    if not sentences:
        return []

    embeddings = model.encode(sentences)

    similarities = []
    for i in range(1, len(embeddings)):
        sim = util.cos_sim(embeddings[i], embeddings[i-1]).item()
        similarities.append(sim)

    threshold = np.mean(similarities) - np.std(similarities) if similarities else 0

    segments = []
    current_segment = sentences[0]

    for i in range(1, len(sentences)):
        if similarities[i-1] < threshold:
            segments.append(current_segment)
            current_segment = sentences[i]
        else:
            current_segment += " " + sentences[i]

    segments.append(current_segment)
    return segments

def process_segments(text, wav_path):
    audio = AudioSegment.from_file(wav_path)
    total_sec = len(audio) / 1000

    segments_text = embedding_segmentation(text)

    if not segments_text:
        return []

    seg_dur = total_sec // len(segments_text)

    final_output = []

    for i, seg in enumerate(segments_text):
        final_output.append({
            "segment_number": i + 1,
            "start_time": format_time(i * seg_dur),
            "end_time": format_time((i + 1) * seg_dur),
            "text": seg,
            "sentiment": get_sentiment(seg),
            "keywords": extract_keywords(seg),
            "summary": summarize_segment(seg)
        })

    return final_output