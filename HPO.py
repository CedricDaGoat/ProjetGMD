import sqlite3

# Chemin vers ton fichier .sqlite
db_path = "HPO/hpo_annotations.sqlite"

# Ouvre la connexion à la base de données
conn = sqlite3.connect(db_path)

# Crée un curseur pour exécuter des requêtes
cursor = conn.cursor()

# Nom de la table dont on veut les colonnes
table_name = "phenotype_annotation"

# Exécute la requête pour obtenir les informations sur les colonnes
cursor.execute(f"PRAGMA table_info({table_name});")

# Récupère les résultats
columns = cursor.fetchall()

# Affiche les colonnes
print(f"Colonnes de la table '{table_name}' :")
for column in columns:
    print(column[1])  # Le deuxième élément du tuple est le nom de la colonne

# Ferme la connexion
conn.close()
