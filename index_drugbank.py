import xml.etree.ElementTree as ET
import pandas as pd
import re
import sys
import os


# Fonction pour analyser le fichier XML de DrugBank
def parse_drugbank_xml(xml_file_path):
    """
    Parse le fichier XML de DrugBank et retourne une liste des médicaments.
    """
    print("Chargement du fichier XML...")
    # Définir l'espace de noms
    ns = {'db': 'http://www.drugbank.ca'}

    # Charger le fichier XML
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Erreur lors de l'analyse du XML: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Le fichier {xml_file_path} n'existe pas.")
        sys.exit(1)

    print(f"XML chargé avec succès. Extraction des médicaments...")

    # Extraire tous les médicaments
    drugs = root.findall('.//db:drug', ns)
    print(f"{len(drugs)} médicaments trouvés.")

    return drugs, ns


# Chargement de la liste des symptômes depuis symtoms_list.py
def load_symptoms_list():
    """
    Charge la liste des symptômes depuis le fichier symtoms_list.py
    """
    try:
        # Importer la fonction depuis le module de symptômes
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from symtoms_list import get_comprehensive_symptoms_list

        # Appeler la fonction pour obtenir la liste des symptômes
        symptoms_list = get_comprehensive_symptoms_list()
        print(f"Liste de {len(symptoms_list)} symptômes chargée.")
        return symptoms_list
    except ImportError:
        print("Impossible de charger la fonction get_comprehensive_symptoms_list depuis symtoms_list.py")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors du chargement des symptômes: {e}")
        sys.exit(1)


# Fonction pour extraire les symptômes du texte
def extract_symptoms_from_text(text, symptoms_list):
    """
    Extrait les mentions de symptômes d'un texte donné en utilisant
    la liste de symptômes fournie.
    """
    if not text or text.strip() == '':
        return []

    found_symptoms = []
    text_lower = text.lower()

    for symptom in symptoms_list:
        # Recherche du symptôme exact avec délimiteurs de mots
        pattern = r'\b' + re.escape(symptom.lower()) + r'\b'
        if re.search(pattern, text_lower):
            found_symptoms.append(symptom)

    return found_symptoms


def main():
    # Chemin du fichier XML DrugBank
    xml_file_path = "DRUGBANK/drugbank.xml"

    # Chemin de sortie pour le CSV
    csv_output_path = "drug_symptoms_relations.csv"

    # Charger la liste de symptômes
    symptoms_list = load_symptoms_list()

    # Parser le fichier XML
    drugs, ns = parse_drugbank_xml(xml_file_path)

    # Préparer la structure de données pour le CSV
    output_data = []

    print("Extraction des relations médicament-symptôme...")
    for i, drug in enumerate(drugs):
        if i % 100 == 0:
            print(f"Traitement du médicament {i + 1}/{len(drugs)}...")

        try:
            # Extraction des informations du médicament
            drug_id = drug.find('./db:drugbank-id[@primary="true"]', ns)
            if drug_id is None:
                # Si aucun ID principal n'est trouvé, utilisez le premier ID
                drug_ids = drug.findall('./db:drugbank-id', ns)
                if not drug_ids:
                    continue
                drug_id = drug_ids[0]
            drug_id = drug_id.text

            drug_name = drug.find('./db:name', ns)
            if drug_name is None or not drug_name.text:
                continue
            drug_name = drug_name.text

            # Extraction des symptômes que le médicament traite (dans l'indication)
            indication = drug.find('./db:indication', ns)
            indication_text = indication.text if indication is not None and indication.text else ""
            treated_symptoms = extract_symptoms_from_text(indication_text, symptoms_list)

            # Extraction des symptômes causés (effets secondaires dans la toxicité)
            toxicity = drug.find('./db:toxicity', ns)
            toxicity_text = toxicity.text if toxicity is not None and toxicity.text else ""
            caused_symptoms = extract_symptoms_from_text(toxicity_text, symptoms_list)

            # Construction des chaînes pour les symptômes traités et causés
            treated_str = "; ".join(treated_symptoms) if treated_symptoms else ""
            caused_str = "; ".join(caused_symptoms) if caused_symptoms else ""

            # Ajouter aux données de sortie
            output_data.append({
                'drug_id': drug_id,
                'drug_name': drug_name,
                'treats': treated_str,
                'causes': caused_str
            })

        except Exception as e:
            print(f"Erreur lors du traitement du médicament {i + 1}: {e}")

    # Créer le DataFrame
    print("Création du DataFrame...")
    df = pd.DataFrame(output_data)

    # Filtrer les entrées sans information utile
    df_filtered = df[(df['treats'] != "") | (df['causes'] != "")]
    print(f"Nombre total de médicaments: {len(df)}")
    print(f"Nombre de médicaments avec au moins un symptôme traité ou causé: {len(df_filtered)}")

    # Enregistrer en CSV
    print(f"Enregistrement du CSV dans {csv_output_path}...")
    df_filtered.to_csv(csv_output_path, index=False)
    print("Terminé !")


if __name__ == "__main__":
    main()
