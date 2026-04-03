import os
from pydub import AudioSegment
import noisereduce as nr
import librosa
import soundfile as sf


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw_audio")
CLEAN_DIR = os.path.join(BASE_DIR, "data", "clean_audio")

def preprocess_audio(file_name):
    input_path = os.path.join(RAW_DIR, file_name)
    
    # converting to .wav format 
    sound = AudioSegment.from_file(input_path)
    wav_name = file_name.rsplit('.', 1)[0] + ".wav"
    wav_path = os.path.join(CLEAN_DIR, wav_name)
    
    sound = sound.set_frame_rate(16000).set_channels(1)
    sound.export(wav_path, format="wav")

    # Noise Reduse
    y, sr = librosa.load(wav_path, sr=16000)
    reduced_noise = nr.reduce_noise(y=y, sr=sr)
    sf.write(wav_path, reduced_noise, sr)
    
    return wav_path 