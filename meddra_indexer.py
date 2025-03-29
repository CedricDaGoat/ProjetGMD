import re
import pandas as pd
import pickle
import csv

def charger_noms_medicaments(fichier_tsv):
    """
    Charge un dictionnaire associant les identifiants des médicaments à leurs noms depuis un fichier TSV.
    
    Args:
        fichier_tsv (str): Chemin du fichier TSV contenant les identifiants et noms de médicaments.
    
    Returns:
        dict: Dictionnaire {id_medicament: nom_medicament}
    """
    noms_medicaments = {}
    with open(fichier_tsv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            if len(row) >= 2:
                id_medicament, nom_medicament = row[0], row[1]
                noms_medicaments[id_medicament] = nom_medicament
    return noms_medicaments

def index_meddra_all_se(file_path, fichier_tsv):
    """
    Crée un index des effets secondaires aux médicaments avec ID et nom.

    Args:
        file_path (str): Chemin du fichier contenant les associations médicament-effet secondaire.
        fichier_tsv (str): Chemin du fichier TSV contenant les noms des médicaments.

    Returns:
        dict: Dictionnaire {symptôme: {(ID, Nom), (ID, Nom), ...}}
    """
    symptom_to_drugs = {}

    # Charger les noms des médicaments
    noms_medicaments = charger_noms_medicaments(fichier_tsv)

    # Expression régulière pour vérifier si l'ID est de la forme CID1xxxxxxxx
    cid_pattern = re.compile(r"^CID1\d{8}$")  # Le format CID1 suivi de 8 chiffres

    # Lecture du fichier ligne par ligne
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            cols = line.strip().split('\t')
            if len(cols) < 6:
                continue  # Ignore les lignes mal formées

            drug_id = cols[0]  # ID du médicament
            symptom = cols[-1]  # Nom de l'effet secondaire (PT)

            # Vérifier si l'ID du médicament est valide
            if not cid_pattern.match(drug_id):
                print(f"ID incorrect trouvé : {drug_id}")

            # Récupérer le nom du médicament ou mettre un placeholder
            drug_name = noms_medicaments.get(drug_id, "Nom inconnu")

            # Ajouter au dictionnaire
            if symptom not in symptom_to_drugs:
                symptom_to_drugs[symptom] = set()
            symptom_to_drugs[symptom].add((drug_id, drug_name))

    return symptom_to_drugs

def save_index_to_disk(index, filename):
    with open(filename, 'wb') as f:
        pickle.dump(index, f)
    print(f"Index sauvegardé dans {filename}")

def load_index_from_disk(filename):
    with open(filename, 'rb') as f:
        index = pickle.load(f)
    print(f"Index chargé depuis {filename}")
    return index

file_path = "SIDER/meddra_all_se.tsv"  # Chemin vers le fichier
index_filename = "SIDER/index_all_se"
try:
    index = load_index_from_disk(index_filename)
except FileNotFoundError:
    index = index_meddra_all_se(file_path, fichier_tsv="SIDER/drug_names.tsv")
    save_index_to_disk(index, index_filename)


file_path = "SIDER/meddra_all_indications.tsv"  # Chemin vers le fichier
index_filename = "SIDER/index_all_indications"
try:
    index = load_index_from_disk(index_filename)
except FileNotFoundError:
    index = index_meddra_all_se(file_path, fichier_tsv="SIDER/drug_names.tsv")
    save_index_to_disk(index, index_filename)



def rechercher_medicaments_meddra(symptomes, index, logique='OU'):
    """
    Recherche des médicaments en fonction des symptômes donnés, avec une option 'ET' ou 'OU'.
    
    Args:
        symptomes (list): Liste des symptômes à rechercher.
        index (dict): Index des symptômes aux médicaments.
        logique (str): 'ET' si tous les symptômes doivent être présents, 'OU' si seulement une partie.
    
    Returns:
        list: Liste des noms des médicaments correspondant à la recherche.
    """
    if not symptomes:  # Vérifie si la liste des symptômes est vide
        return []

    # Récupérer la liste des sets de médicaments associés à chaque symptôme
    medicaments_par_symptome = [index.get(symptome, set()) for symptome in symptomes]

    # Supprimer les ensembles vides (pour éviter les problèmes avec l'intersection)
    medicaments_par_symptome = [med for med in medicaments_par_symptome if med]

    if not medicaments_par_symptome:  # Si aucun symptôme n'a donné de médicaments
        return []

    # Cas 'ET' : Trouver l'intersection de tous les médicaments (médicaments communs à tous les symptômes)
    if logique == 'ET':
        resultats = set.intersection(*medicaments_par_symptome)
    # Cas 'OU' : Trouver l'union de tous les médicaments (médicaments liés à au moins un symptôme)
    else:
        resultats = set.union(*medicaments_par_symptome)

    # EXTRAIRE UNIQUEMENT LES NOMS DES MÉDICAMENTS
    return sorted({nom for _, nom in resultats})

def rechercher_medicaments_indic_meddra(symptomes, index, logique='OU'):
    """
    Recherche des médicaments en fonction des symptômes donnés, avec une option 'ET' ou 'OU'.
    
    Args:
        symptomes (list): Liste des symptômes à rechercher.
        index (dict): Index des symptômes aux médicaments.
        logique (str): 'ET' si tous les symptômes doivent être présents, 'OU' si seulement une partie.
    
    Returns:
        list: Liste des noms des médicaments correspondant à la recherche.
    """
    if not symptomes:  # Vérifie si la liste des symptômes est vide
        return []

    # Récupérer la liste des sets de médicaments associés à chaque symptôme
    medicaments_par_symptome = [index.get(symptome, set()) for symptome in symptomes]

    # Supprimer les ensembles vides (pour éviter les problèmes avec l'intersection)
    medicaments_par_symptome = [med for med in medicaments_par_symptome if med]

    if not medicaments_par_symptome:  # Si aucun symptôme n'a donné de médicaments
        return []

    # Cas 'ET' : Trouver l'intersection de tous les médicaments (médicaments communs à tous les symptômes)
    if logique == 'ET':
        resultats = set.intersection(*medicaments_par_symptome)
    # Cas 'OU' : Trouver l'union de tous les médicaments (médicaments liés à au moins un symptôme)
    else:
        resultats = set.union(*medicaments_par_symptome)

    # EXTRAIRE UNIQUEMENT LES NOMS DES MÉDICAMENTS
    return sorted({nom for _, nom in resultats})
