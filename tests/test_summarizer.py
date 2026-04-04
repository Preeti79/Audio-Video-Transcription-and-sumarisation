from backend.segmentation.summarizer import summarize_segment

def test_summarizer():
    text = " ".join(["AI is transforming the world."] * 20)
    print(summarize_segment(text))

if __name__ == "__main__":
    test_summarizer()