from backend.segmentation.segmentation import process_segments
import os

def test_process_segments():
    print("Segmentation test started...")

    
    dummy_text = (
        "This is the first sentence. "
        "This is the second sentence. "
        "This is the third sentence. "
        "This is the fourth sentence."
    )

    
    test_audio = "backend/data/clean_audio/eps_6.wav"

    if not os.path.exists(test_audio):
        print("Test audio file not found")
        return

    
    segments = process_segments(dummy_text, test_audio)

    print("Segments Output:", segments)

   
    assert isinstance(segments, list)
    assert len(segments) > 0

    seg = segments[0]

    assert "segment_number" in seg
    assert "start_time" in seg
    assert "end_time" in seg
    assert "text" in seg
    assert "sentiment" in seg
    assert "keywords" in seg
    assert "summary" in seg

    print("Test passed ✅")


if __name__ == "__main__":
    test_process_segments()