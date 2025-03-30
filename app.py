from flask import Flask, render_template, request
import os
import pandas as pd
from OMIM import split_and_parse_records, search_records
from search_drugbank import recherche_medicaments_par_symptomes
app = Flask(__name__)


# Chemin pour OMIM
OMIM_PATH = "OMIM/omim.txt"
omim_records = split_and_parse_records(OMIM_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    drugs_causing = []
    drugs_treating = []
    genetic_diseases = []
    symptoms_list = []
    condition = "OU"

    if request.method == 'POST':
        # Récupérer les symptômes saisis par l'utilisateur
        symptoms_input = request.form.get("symptoms", "")
        symptoms_list = [symptom.strip() for symptom in symptoms_input.split(',') if symptom.strip()]

        # Vérifier si la checkbox "ET" est cochée
        condition = "ET" if request.form.get("and_condition") == "on" else "OU"

        # Appeler notre nouvelle fonction qui utilise le CSV
        if symptoms_list:
            drugs_causing, drugs_treating = recherche_medicaments_par_symptomes(symptoms_list, condition)
            genetic_diseases = search_records(omim_records, symptoms_list, condition)

    # Renvoyer les résultats à la page HTML
    return render_template('index.html',
                           drugs_causing=drugs_causing,
                           drugs_treating=drugs_treating,
                           genetic_diseases=genetic_diseases,
                           symptoms=", ".join(symptoms_list),
                           condition=condition)

