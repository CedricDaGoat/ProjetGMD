import sqlite3



def explorer_base_de_donnees(db_path):
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        print(f"Connecté à la base de données '{db_path}'.")

        # Récupérer la liste des tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        print("\nTables disponibles dans la base de données:")
        for i, table in enumerate(tables, 1):
            print(f"  {i}. {table}")

        # Récupérer et afficher la structure de chaque table
        for table in tables:
            print(f"\nStructure de la table '{table}':")
            cursor.execute(f"PRAGMA table_info({table})")
            columns = cursor.fetchall()
            for column in columns:
                col_id, col_name, col_type, not_null, default_val, pk = column
                print(f"  - {col_name} ({col_type}){' PRIMARY KEY' if pk else ''}")

            # Compter les enregistrements
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"  Nombre total d'enregistrements: {count}")

        # Fermer la connexion
        conn.close()
        print("\nExploration terminée.")
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")


if __name__ == "__main__":

    explorer_base_de_donnees("HPO/hpo_annotations.sqlite")
