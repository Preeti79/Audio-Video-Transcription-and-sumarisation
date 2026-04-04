from backend.segmentation.keywords import extract_keywords

def test_keywords():
    text = "Machine learning is a powerful tool in artificial intelligence"
    print(extract_keywords(text))

if __name__ == "__main__":
    test_keywords()