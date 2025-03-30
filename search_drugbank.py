import pandas as pd
import os
# Chemin vers le fichier CSV
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "drug_symptoms_relations.csv")

def recherche_medicaments_par_symptomes(symptomes, operateur, csv_path="drug_symptoms_relations.csv"):
    """
    Recherche les médicaments qui traitent ou causent des symptômes selon un opérateur logique.

    Args:
        symptomes (list): Liste des symptômes à rechercher
        operateur (str): "ET" ou "OU" pour la recherche
        csv_path (str): Chemin vers le fichier CSV des médicaments

    Returns:
        dict: Dictionnaire avec deux listes (médicaments qui soignent, médicaments qui causent)
    """
    # Charger le CSV
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return {"error": f"Erreur lors du chargement du CSV: {str(e)}"}

    # Normaliser les symptômes
    symptomes = [s.lower().strip() for s in symptomes if s.strip()]
    if not symptomes:
        return {"error": "Aucun symptôme valide fourni"}

    medicaments_soignant = []
    medicaments_causant = []

    # Pour chaque médicament dans le DataFrame
    for _, row in df.iterrows():
        drug_id = row['drug_id']
        drug_name = row['drug_name']

        # Extraire les symptômes traités et causés
        treats_symptoms = []
        if pd.notna(row['treats']) and isinstance(row['treats'], str):
            treats_symptoms = [s.lower().strip() for s in row['treats'].split(';') if s.strip()]

        causes_symptoms = []
        if pd.notna(row['causes']) and isinstance(row['causes'], str):
            causes_symptoms = [s.lower().strip() for s in row['causes'].split(';') if s.strip()]

        # Vérifier les correspondances selon l'opérateur logique
        if operateur.upper() == "ET":
            # Tous les symptômes doivent être présents
            if all(s in treats_symptoms for s in symptomes):
                medicaments_soignant.append({"id": drug_id, "name": drug_name})
            if all(s in causes_symptoms for s in symptomes):
                medicaments_causant.append({"id": drug_id, "name": drug_name})
        else:  # "OU" par défaut
            # Au moins un symptôme doit être présent
            if any(s in treats_symptoms for s in symptomes):
                medicaments_soignant.append({"id": drug_id, "name": drug_name})
            if any(s in causes_symptoms for s in symptomes):
                medicaments_causant.append({"id": drug_id, "name": drug_name})

    return {
        "query": {
            "symptomes": symptomes,
            "operateur": operateur
        },
        "resultats": {
            "medicaments_soignant": medicaments_soignant,
            "medicaments_causant": medicaments_causant
        }
    }

def recherche_medicaments_par_symptomes(symptomes, operateur, csv_path=CSV_PATH):
    """
    Recherche les médicaments qui traitent ou causent des symptômes selon un opérateur logique.

    Args:
        symptomes (list): Liste des symptômes à rechercher
        operateur (str): "ET" ou "OU" pour la recherche
        csv_path (str): Chemin vers le fichier CSV des médicaments

    Returns:
        tuple: Deux listes (médicaments qui causent, médicaments qui soignent)
    """
    # Charger le CSV
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Erreur lors du chargement du CSV: {str(e)}")
        return [], []

    # Normaliser les symptômes
    symptomes = [s.lower().strip() for s in symptomes if s.strip()]
    if not symptomes:
        return [], []

    medicaments_soignant = []
    medicaments_causant = []

    # Pour chaque médicament dans le DataFrame
    for _, row in df.iterrows():
        drug_id = row['drug_id']
        drug_name = row['drug_name']

        # Extraire les symptômes traités et causés
        treats_symptoms = []
        if pd.notna(row['treats']) and isinstance(row['treats'], str):
            treats_symptoms = [s.lower().strip() for s in row['treats'].split(';') if s.strip()]

        causes_symptoms = []
        if pd.notna(row['causes']) and isinstance(row['causes'], str):
            causes_symptoms = [s.lower().strip() for s in row['causes'].split(';') if s.strip()]

        # Vérifier les correspondances selon l'opérateur logique
        if operateur.upper() == "ET":
            # Tous les symptômes doivent être présents
            if all(s in treats_symptoms for s in symptomes):
                medicaments_soignant.append((drug_id, drug_name))
            if all(s in causes_symptoms for s in symptomes):
                medicaments_causant.append((drug_id, drug_name))
        else:  # "OU" par défaut
            # Au moins un symptôme doit être présent
            if any(s in treats_symptoms for s in symptomes):
                medicaments_soignant.append((drug_id, drug_name))
            if any(s in causes_symptoms for s in symptomes):
                medicaments_causant.append((drug_id, drug_name))

    return medicaments_causant, medicaments_soignant
