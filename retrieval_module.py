
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_email(email):
    try:
        df = pd.read_csv("data/emails.csv").fillna("")

        emails = df["Customer_Email"].astype(str).tolist()

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(emails + [email])

        scores = cosine_similarity(
            vectors[-1], vectors[:-1]
        ).flatten()

        index = scores.argmax()

        previous_email = emails[index]
        previous_reply = df.iloc[index]["Previous_Reply"]

        print("\n===== SIMILAR EMAIL =====")
        print("Previous Email:", previous_email)
        print("Previous Reply:", previous_reply)

        return str(previous_reply)

    except Exception as e:
        print("Retrieval error:", e)
        return "We will review your concern and assist you shortly."
