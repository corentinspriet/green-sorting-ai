# 🗑️ Green Waste Classifier — Tri intelligent de déchets avec BERT

> Projet NLP & classification multi-classes | Python · Transformers · Deep Learning 

Dans le cadre de mon autoformation, j'ai réalisé ce projet qui vise à classifier automatiquement des déchets à partir de descriptions textuelles courtes. Il utilise un modèle BERT multilingue fine-tuné sur un dataset textuel de 1000 entrées.

---

## 🎯 Objectifs du projet

- Classifier un déchet à partir d'une description comme : `"bouteille en plastique transparente"`
- Explorer des modèles de NLP performants sur un dataset modeste
- Appliquer des bonnes pratiques ML (prétraitement, validation, équilibre des classes)

---

## 🧠 Modèle utilisé

- **BERT (bert-base-multilingual-cased)** — pré-entraîné, fine-tuné sur 8 classes de déchets
- Tokenisation avec `transformers`
- Classification multi-classes avec PyTorch et `Trainer` de Hugging Face

---

## 📂 Structure du projet

green-waste-classifier/
├── data/
│ └── dechets.json # Dataset textuel étiqueté
├── notebook/
│ └── bert_classifier.ipynb # Notebook principal
├── requirements.txt # Dépendances du projet
└── README.md # Ce fichier

## 📊 Résultats

## 📊 Résultats

| Classe            | Précision | Rappel | F1-score | Support |
|-------------------|-----------|--------|----------|---------|
| Compost           | 1.00      | 1.00   | 1.00     | 33      |
| Métal             | 1.00      | 1.00   | 1.00     | 33      |
| Non-recyclable    | 1.00      | 1.00   | 1.00     | 33      |
| Papier/Carton     | 1.00      | 1.00   | 1.00     | 34      |
| Plastique         | 0.87      | 1.00   | 0.93     | 34      |
| Verre             | 1.00      | 0.85   | 0.92     | 33      |

### ✅ Accuracy globale : **97%**
Grace à l'extension du dataset et l'intégration de BERT (via transformers), le modèle est désormais très performant, avec une excellente généralisation sur toutes les classes, y compris les plus difficiles comme plastique et verre.

---

## 🧪 Tester une prédiction

```python
predire_description("canette de soda en aluminium")
# → "métal"
🚀 Lancer le projet
Cloner le repo :
git clone https://github.com/corentinspriet/green-waste-classifier.git
cd green-waste-classifier
Installer les dépendances :
pip install -r requirements.txt
Ouvrir le notebook :

jupyter notebook notebook/bert_classifier.ipynb
🛠️ Améliorations possibles
✅ Ajout de données : + d’exemples équilibrés

✅ Data augmentation : synonymes, traductions

🔄 Entraînement plus long ou modèle DistilBERT pour plus de légèreté

🖼️ Création d’une UI avec Streamlit pour tester en ligne

🧩 API Flask ou FastAPI pour intégration dans un système de tri

👨‍💻 Auteur
[Corentin Spriet] — Développeur junior passionné de data science & IA
En recherche de stage en Machine Learning / Data Science / Software Engineer