import re


def parse_record(record_text):
    """Extrait les champs NO, TI, DESCRIPTION, et CS d'un enregistrement."""
    no = re.findall(r"\*FIELD\* NO\n(.+)", record_text)
    ti = re.findall(r"\*FIELD\* TI\n(.+)", record_text)
    description = re.findall(r"\*FIELD\* TX\n(.+?)(?=\*FIELD\*|\Z)", record_text, re.DOTALL)
    cs = re.findall(r"\*FIELD\* CS\n(.+?)(?=\*FIELD\*|\Z)", record_text, re.DOTALL)
    
    no = no[0].strip() if no else None
    ti = ti[0].strip() if ti else None
    description = description[0].strip() if description else None
    cs = cs[0].strip() if cs else None

    return {"NO": no, "TI": ti, "DESCRIPTION": description, "CS": cs}


def split_and_parse_records(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # On découpe en enregistrements par "*RECORD*"
    raw_records = content.split('*RECORD*')
    parsed_records = []
    
    for record in raw_records:
        record = record.strip()
        if record:
            parsed_records.append(parse_record(record))
    
    return parsed_records

OMIM_PATH = "OMIM/omim.txt"

omim_records = split_and_parse_records(OMIM_PATH)

def search_records(records, symptoms_list, mode="OU"):
    """
    Recherche des enregistrements contenant des symptômes.

    Args:
        records (list): Liste des enregistrements parsés.
        symptoms_list (list): Liste des symptômes recherchés.
        mode (str): "OU" (par défaut) ou "ET" pour le type de recherche.

    Returns:
        list: Liste des enregistrements correspondants.
    """
    results = []
    
    for record in records:
        if record.get("CS"):  # Vérifier si "CS" est présent et non vide
            # Nettoyage des lignes des symptômes
            cs_lines = [line.strip() for line in record["CS"].split('\n') if line.strip() and not line.strip().endswith(":")]

            # Vérifier chaque symptôme et stocker ceux trouvés
            symptoms_found = set()
            
            for symptom in symptoms_list:
                symptom_lower = symptom.lower().strip()

                # Vérifier si le symptôme est présent dans *au moins* une ligne et n'est pas précédé de "no"
                found = any(
                    symptom_lower in line.lower() and not re.search(rf"\bno {re.escape(symptom_lower)}\b", line.lower())
                    for line in cs_lines
                )

                if found:
                    symptoms_found.add(symptom)

            # Vérifier si on doit inclure ce record en fonction du mode
            if (mode == "OU" and symptoms_found) or (mode == "ET" and len(symptoms_found) == len(symptoms_list)):
                clean_cs_lines = [
                    line for line in cs_lines if not line.strip().endswith(":") and "[" not in line and "]" not in line
                ]

                results.append({
                    "TI": record.get("TI", ""),
                    "DESCRIPTION": record.get("DESCRIPTION", ""),
                    "SYMPTOMS_FOUND": list(symptoms_found),
                    "ALL_SYMPTOMS": clean_cs_lines  # Liste propre des symptômes filtrés
                })

    return results

