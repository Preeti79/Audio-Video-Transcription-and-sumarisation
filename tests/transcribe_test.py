from backend.transcription.transcribe import get_transcription
import os

def transcribe_test():
    test_audio = "backend/data/clean_audio/eps_6.wav" 

    if not os.path.exists(test_audio):
        print("Test audio file not found")
        return

    text = get_transcription(test_audio)

    print("Transcription:", text)

    assert isinstance(text, str)
    assert len(text) > 0

if __name__ == "__main__":
    transcribe_test()