
import pandas as pd

"""
Lire ton fichier main_phenotype_annotation.csv

Lire le fichier hpo.obo

Extraire tous les symptômes en noms humains

Générer un fichier symptom_list.py contenant une fonction get_symptoms() qui retourne la liste
"""
# Charger le fichier CSV contenant les annotations phénotypiques
df = pd.read_csv("HPO/main_phenotype_annotation.csv")

# Extraire tous les HPO_ID uniques
all_hpo_ids = df["HP:0000252"].dropna().unique()

# Charger le fichier hpo.obo et créer un dictionnaire de mapping HPO_ID → nom
hpo_mapping = {}
current_id = None

with open("HPO/hpo.obo", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line.startswith("id: HP:"):
            current_id = line.split("id: ")[1]
        elif line.startswith("name:") and current_id:
            current_name = line.split("name: ")[1]
            hpo_mapping[current_id] = current_name
            current_id = None

# Traduire tous les HPO_ID en noms
translated_symptoms = [hpo_mapping.get(hpo, hpo) for hpo in all_hpo_ids]

# Garder uniquement les noms traduits (exclure les codes bruts)
translated_symptoms_clean = sorted(set(s for s in translated_symptoms if not s.startswith("HP:")))

# Générer le code Python contenant la liste
with open("symptom_list.py", "w", encoding="utf-8") as f:
    f.write("def get_symptoms():\n")
    f.write("    return [\n")
    for symptom in translated_symptoms_clean:
        f.write(f'        "{symptom}",\n')
    f.write("    ]\n")

print("symptom_list.py généré avec succès.")
