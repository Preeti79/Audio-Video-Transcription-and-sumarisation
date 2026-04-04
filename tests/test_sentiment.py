from backend.segmentation.sentiment import get_sentiment

def test_sentiment():
    print(get_sentiment("I love this product"))
    print(get_sentiment("This is very bad"))
    print(get_sentiment("It is okay"))

if __name__ == "__main__":
    test_sentiment()