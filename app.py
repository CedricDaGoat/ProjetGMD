from flask import Flask, render_template, request
import os
from drug_bank import get_drugs_for_symptoms  # Import de la fonction
from OMIM import split_and_parse_records, search_records
from meddra_indexer import load_index_from_disk, rechercher_medicaments_meddra, rechercher_medicaments_indic_meddra


app = Flask(__name__)

# Chemin vers le fichier XML (assurez-vous qu'il existe dans ce chemin)
DRUGBANK_FILE_PATH = os.path.join("DRUGBANK", "drugbank.xml")
OMIM_PATH = "OMIM/omim.txt"
omim_records = split_and_parse_records(OMIM_PATH)

@app.route('/', methods=['GET', 'POST'])
def index():
    drugs_causing = []
    drugs_treating = []
    genetic_diseases = []
    if request.method == 'POST':
        # Récupérer les symptômes saisis par l'utilisateur
        symptoms_input = request.form.get("symptoms")  # Exemple : "headache, nausea"
        symptoms_list = [symptom.strip() for symptom in symptoms_input.split(',')]

        # Vérifier si la checkbox "ET" est cochée
        condition = "ET" if request.form.get("and_condition") == "on" else "OU"
        index_se_name = "SIDER/index_all_se"
        index_se = load_index_from_disk(index_se_name)
        index_ind_name = "SIDER/index_all_indications"  
        index_all_indications = load_index_from_disk(index_ind_name)
        # Appeler la fonction de traitement avec les paramètres
        drugs_causing, drugs_treating = rechercher_medicaments_meddra(symptoms_list, index_se, condition),rechercher_medicaments_indic_meddra(symptoms_list, index_all_indications, condition)#get_drugs_for_symptoms(symptoms_list, DRUGBANK_FILE_PATH, condition)
        genetic_diseases = search_records(omim_records, symptoms_list, condition)
    


    # Renvoyer les résultats à la page HTML
    return render_template('index.html', drugs_causing=drugs_causing, drugs_treating=drugs_treating, genetic_diseases=genetic_diseases)


if __name__ == '__main__':
    # Lancer l'application Flask
    app.run(debug=True)
