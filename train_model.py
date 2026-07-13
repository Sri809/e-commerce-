import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_dataset.csv")

# Combine important text columns
df["tags"] = (
    df["name"].fillna("") + " " +
    df["brand"].fillna("") + " " +
    df["categories"].fillna("")
)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["tags"])

# Cosine Similarity
similarity = cosine_similarity(tfidf_matrix)

# Save files
pickle.dump(similarity, open("similarity.pkl", "wb"))
pickle.dump(df, open("products.pkl", "wb"))
pickle.dump(tfidf, open("model.pkl", "wb"))

print("===================================")
print("Model Training Completed Successfully!")
print("===================================")
print("Files Created:")
print("1. model.pkl")
print("2. similarity.pkl")
print("3. products.pkl")