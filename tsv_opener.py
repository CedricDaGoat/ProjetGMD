# ouvrir_n_premieres_lignes_tsv.py

def afficher_n_premieres_lignes(file_path, n):
    """
    Affiche les n premières lignes du fichier TSV.
    
    Args:
        file_path (str): Le chemin du fichier TSV.
        n (int): Le nombre de lignes à afficher.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Lire les n premières lignes du fichier
            for i in range(n):
                ligne = f.readline().strip()
                if ligne:  # Si la ligne n'est pas vide
                    print(f"Ligne {i + 1}: {ligne}")
                else:
                    break  # Si on atteint la fin du fichier avant n lignes
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    file_path = "STITCH - ATC/chemical.sources.v5.0.tsv"  # Remplace par le chemin vers ton fichier
    n = 20  # Remplace par le nombre de lignes que tu veux afficher
    afficher_n_premieres_lignes(file_path, n)
