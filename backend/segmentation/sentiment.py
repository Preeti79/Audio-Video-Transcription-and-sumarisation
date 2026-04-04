from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score > 0.1:
        return "POSITIVE"
    elif score < -0.1:
        return "NEGATIVE"
    else:
        return "NEUTRAL"