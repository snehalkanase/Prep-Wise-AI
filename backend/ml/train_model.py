import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("ml/jd_question_dataset.csv")

# Input features = JD text
X = df["jd"]

# Output = questions (joined as one string for now)
y = df["questions"]

# Convert JD text to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
X_vectorized = vectorizer.fit_transform(X)

# Train a simple classifier
model = LogisticRegression()
model.fit(X_vectorized, y)

# Save model and vectorizer
pickle.dump(model, open("ml/question_model.pkl", "wb"))
pickle.dump(vectorizer, open("ml/vectorizer.pkl", "wb"))

print("✅ Model trained and saved!")
