# data.py

def Seeker(query_list):
    # Simuler une recherche et retourner une liste de listes
    # Chaque sous-liste représente un médicament avec ses infos
    medicaments = [
        ["Paracétamol", "500mg", "Soulage la douleur et la fièvre"],
        ["Ibuprofène", "200mg", "Anti-inflammatoire et analgésique"],
        ["Aspirine", "300mg", "Traitement de la douleur légère"],
    ]

    # Exemple : filtrer les médicaments par un match (ici simple pour la démo)
    resultat = []
    for med in medicaments:
        for char in query_list:
            if char.lower() in med[0].lower():  # Rechercher la correspondance
                resultat.append(med)
                break  # Éviter les doublons
    return resultat
