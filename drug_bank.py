# drug_bank.py
import xml.etree.ElementTree as ET

def Seeker(query_list):
    # Grande liste de médicaments avec leurs noms, dosages et descriptions
    medicaments = [
        ["Paracétamol", "500mg", "Soulage la douleur et la fièvre courante."],
        ["Ibuprofène", "200mg", "Anti-inflammatoire non stéroïdien."],
        ["Aspirine", "300mg", "Utilisé pour la douleur légère et la fièvre."],
        ["Amoxicilline", "500mg", "Antibiotique utilisé pour traiter les infections bactériennes."],
        ["Cétirizine", "10mg", "Antihistaminique pour traiter les allergies."],
        ["Oméprazole", "20mg", "Traite les reflux acides et les ulcères gastriques."],
        ["Simvastatine", "10mg", "Réduit le cholestérol et prévient les maladies cardiaques."],
        ["Atorvastatine", "20mg", "Diminue le mauvais cholestérol et les triglycérides."],
        ["Metformine", "850mg", "Traitement pour le diabète de type 2."],
        ["Salbutamol", "100µg", "Utilisé pour traiter l'asthme et les maladies respiratoires."],
        ["Losartan", "50mg", "Antihypertenseur pour réduire la tension artérielle."],
        ["Ramipril", "10mg", "Réduit la tension artérielle et protège les reins."],
        ["Antalgiques codéinés", "30mg", "Traitement de la douleur modérée à sévère."],
        ["Clarithromycine", "500mg", "Antibiotique pour les infections respiratoires et cutanées."],
        ["Furosémide", "40mg", "Diurétique utilisé pour réduire l'œdème et l'hypertension."],
        ["Levothyroxine", "50µg", "Traite l'insuffisance thyroïdienne (hypothyroïdie)."],
        ["Prednisone", "20mg", "Corticostéroïde utilisé pour traiter les allergies et inflammations."],
        ["Alprazolam", "0.5mg", "Utilisé pour l'anxiété et les troubles paniques."],
        ["Diazépam", "5mg", "Anxiolytique et relaxant musculaire."],
        ["Fluoxetine", "20mg", "Antidépresseur utilisé pour traiter la dépression et l'anxiété."],
        ["Loratadine", "10mg", "Antihistaminique pour soulager les symptômes d'allergie."],
        ["Clopidogrel", "75mg", "Prévient les caillots sanguins chez les patients à risque."],
        ["Escitalopram", "10mg", "Antidépresseur utilisé pour les troubles anxieux et dépressifs."],
        ["Rosuvastatine", "10mg", "Utilisé pour traiter le cholestérol élevé."],
        ["Tramadol", "50mg", "Traitement de la douleur modérée à sévère."],
        ["Morphine", "10mg", "Traitement de la douleur sévère."],
        ["Propranolol", "40mg", "Bêta-bloquant utilisé pour traiter l'hypertension et l'anxiété."],
        ["Hydrochlorothiazide", "25mg", "Diurétique utilisé pour contrôler la pression artérielle."],
        ["Ciprofloxacine", "500mg", "Antibiotique utilisé pour traiter les infections bactériennes."],
        ["Lamotrigine", "100mg", "Traitement de l'épilepsie et des troubles bipolaires."],
        ["Risperidone", "2mg", "Antipsychotique utilisé pour traiter la schizophrénie et le trouble bipolaire."],
        ["Metoprolol", "50mg", "Bêta-bloquant utilisé pour traiter l'hypertension et les problèmes cardiaques."],
        ["Budesonide", "200µg", "Corticostéroïde utilisé pour l'asthme et la rhinite allergique."],
    ]

    # Exemple : filtrer les médicaments par un match (ici simple pour la démo)
    resultat = []
    for med in medicaments:
        for char in query_list:
            if char.lower() in med[0].lower():  # Rechercher la correspondance
                resultat.append(med)
                break  # Éviter les doublons
    return resultat



def deases_association () :
    return True

def drug_symptosis () :
    return True

def drug_to_cure() :
    return True

def rechercher_medicaments_par_symptomes(fichier_xml, symptomes):
    """
    Recherche les médicaments correspondant à une liste de symptômes dans les indications d'un fichier DrugBank.

    :param fichier_xml: Chemin vers le fichier DrugBank XML.
    :param symptomes: Liste de symptômes à rechercher.
    :return: Liste des médicaments correspondant aux symptômes.
    """
    try:
        # Charger le fichier XML
        tree = ET.parse(fichier_xml)
        root = tree.getroot()

        # Espace de noms utilisé dans la base DrugBank
        namespace = {'ns': 'http://www.drugbank.ca'}

        # Liste des médicaments correspondants
        medicaments_correspondants = []

        # Parcourir tous les médicaments de la base
        for drug in root.findall('ns:drug', namespace):
            # Chercher le nom du médicament
            nom_medicament = drug.find('ns:name', namespace).text

            # Vérifier l'indication (élément <indication>)
            indication_element = drug.find('ns:indication', namespace)
            if indication_element is not None and indication_element.text:
                # Convertir en minuscule et vérifier l'indication
                indication = indication_element.text.lower()
                if any(symptome.lower() in indication for symptome in symptomes):
                    medicaments_correspondants.append(nom_medicament)

        return medicaments_correspondants

    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier_xml} est introuvable.")
        return []
    except ET.ParseError:
        print("Erreur : Le fichier XML est mal formé.")
        return []

def get_drugs_for_symptoms(symptoms, file_path, condition="OU"):
    """
    Prend une liste de symptômes en entrée et retourne :
    1. Une liste de médicaments causant ces symptômes.
    2. Une liste de médicaments traitant ces symptômes.

    Le paramètre condition détermine le mode de recherche :
    - "OU" : Médicaments correspondant à au moins un des symptômes donnés.
    - "ET" : Médicaments correspondant à tous les symptômes donnés.
    """
    # Analyse du fichier XML pour créer les index
    symptoms_to_drugs, treatments_to_drugs = parse_drugbank_xml(file_path)

    # Résultats intermédiaires
    drugs_causing_symptoms_list = []
    drugs_treating_symptoms_list = []

    for symptom in symptoms:
        symptom_lower = symptom.lower()
        # Ajouter les médicaments causant ce symptôme
        drugs_causing_symptoms_list.append(set(symptoms_to_drugs.get(symptom_lower, [])))
        # Ajouter les médicaments traitant ce symptôme
        drugs_treating_symptoms_list.append(set(treatments_to_drugs.get(symptom_lower, [])))

    # Traitement conditionnel
    if condition == "ET":
        # Intersection : Médicaments qui causent ou traitent TOUS les symptômes
        drugs_causing_symptoms = set.intersection(
            *drugs_causing_symptoms_list) if drugs_causing_symptoms_list else set()
        drugs_treating_symptoms = set.intersection(
            *drugs_treating_symptoms_list) if drugs_treating_symptoms_list else set()
    else:  # Par défaut, mode "OU"
        # Union : Médicaments qui causent ou traitent AU MOINS un des symptômes
        drugs_causing_symptoms = set.union(*drugs_causing_symptoms_list) if drugs_causing_symptoms_list else set()
        drugs_treating_symptoms = set.union(*drugs_treating_symptoms_list) if drugs_treating_symptoms_list else set()

    # Retourner les résultats sous forme de liste
    return list(drugs_causing_symptoms), list(drugs_treating_symptoms)


def parse_drugbank_xml(file_path):
    """
    Analyse le fichier XML et retourne deux index :
    1. Médicaments par symptômes qu'ils causent.
    2. Médicaments par indications (ce qu'ils traitent).
    """
    # Chargement et parsing du fichier XML
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Espaces de noms dans le fichier XML
    namespace = {'ns': 'http://www.drugbank.ca'}

    # Dictionnaires pour indexer les données
    symptoms_to_drugs = {}  # Symptômes causés -> Médicaments
    treatments_to_drugs = {}  # Symptômes traités -> Médicaments

    # Parcourir les éléments <drug>
    for drug in root.findall('ns:drug', namespace):
        # Nom du médicament
        drug_name = drug.find('ns:name', namespace).text

        # Indications (ce que traite le médicament)
        indication = drug.find('ns:indication', namespace)
        if indication is not None and indication.text:
            indication_text = indication.text.lower()
            for symptom in indication_text.split():
                treatments_to_drugs.setdefault(symptom, []).append(drug_name)

        # Toxicité / Effets secondaires (ce que le médicament cause)
        toxicity = drug.find('ns:toxicity', namespace)
        if toxicity is not None and toxicity.text:
            toxicity_text = toxicity.text.lower()
            for symptom in toxicity_text.split():
                symptoms_to_drugs.setdefault(symptom, []).append(drug_name)

    return symptoms_to_drugs, treatments_to_drugs

# Chemin vers le fichier XML
file_path = "DRUGBANK/drugbank.xml"

# Liste des symptômes en entrée
symptoms_input = ["headache", "nausea"]

# Mode de recherche (choisir "ET" ou "OU")
condition = "OU"

# Appel de la fonction
drugs_causing, drugs_treating = get_drugs_for_symptoms(symptoms_input, file_path, condition)
#print(drugs_causing,"\n", drugs_treating)

