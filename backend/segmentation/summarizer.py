from transformers import BartTokenizer, BartForConditionalGeneration


tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")


def summarize_segment(text):
    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=70, min_length=30)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary