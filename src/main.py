from classifier import WasteClassifier
import os

DATA_PATH = os.path.join("..", "data", "dechets.json")

def main():
    clf = WasteClassifier(DATA_PATH)
    clf.train()

    print("\n🔍 Entrez une description de déchet (ou 'q' pour quitter) :")
    while True:
        user_input = input("> ")
        if user_input.lower() == "q":
            break
        prediction = clf.predict(user_input)
        print(f"📦 Catégorie prédite : {prediction}\n")

if __name__ == "__main__":
    main()
