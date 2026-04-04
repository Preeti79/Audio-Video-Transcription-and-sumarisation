from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(segment):
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([segment])
        scores = tfidf_matrix.toarray()[0]

        word_scores = list(zip(vectorizer.get_feature_names_out(), scores))
        sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)

        return [w[0].upper() for w in sorted_words[:4]]
    except:
        return []