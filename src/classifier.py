import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

class WasteClassifier:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.model = None

    def load_data(self):
        with open(self.data_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        texts = [item["description"] for item in raw]
        labels = [item["label"] for item in raw]
        return texts, labels

    def train(self):
        texts, labels = self.load_data()
        self.model = make_pipeline(
            TfidfVectorizer(),
            LogisticRegression(max_iter=200)
        )
        self.model.fit(texts, labels)
        print("✅ Modèle entraîné")

    def predict(self, text: str):
        if not self.model:
            raise ValueError("Le modèle n'est pas encore entraîné.")
        return self.model.predict([text])[0]
