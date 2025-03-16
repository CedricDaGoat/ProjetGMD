from flask import Flask, render_template, request
import os
from drug_bank import get_drugs_for_symptoms  # Import de la fonction

app = Flask(__name__)

# Chemin vers le fichier XML (assurez-vous qu'il existe dans ce chemin)
DRUGBANK_FILE_PATH = os.path.join("DRUGBANK", "drugbank.xml")


@app.route('/', methods=['GET', 'POST'])
def index():
    drugs_causing = []
    drugs_treating = []

    if request.method == 'POST':
        # Récupérer les symptômes saisis par l'utilisateur
        symptoms_input = request.form.get("symptoms")  # Exemple : "headache, nausea"
        symptoms_list = [symptom.strip() for symptom in symptoms_input.split(',')]

        # Vérifier si la checkbox "ET" est cochée
        condition = "ET" if request.form.get("and_condition") == "on" else "OU"

        # Appeler la fonction de traitement avec les paramètres
        drugs_causing, drugs_treating = get_drugs_for_symptoms(symptoms_list, DRUGBANK_FILE_PATH, condition)

    # Renvoyer les résultats à la page HTML
    return render_template('index.html', drugs_causing=drugs_causing, drugs_treating=drugs_treating)


if __name__ == '__main__':
    # Lancer l'application Flask
    app.run(debug=True)
