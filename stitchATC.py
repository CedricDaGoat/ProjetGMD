import re

def charger_association_cid_atc(file_path):
    """
    Charge les associations CID à ATC depuis un fichier TSV.
    
    Args:
        file_path (str): Le chemin du fichier TSV contenant les associations CID à ATC.
    
    Returns:
        dict: Un dictionnaire où les clés sont les CID et les valeurs sont les codes ATC correspondants.
    """
    cid_to_atc = {}
    
    # Expression régulière pour vérifier si l'ID est de la forme CID1xxxxxxxx
    cid_pattern = re.compile(r"^CID1\d{8}$")  # Le format CID1 suivi de 8 chiffres
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Ignorer les lignes de commentaires (commençant par #)
            if line.startswith('#'):
                continue
            
            cols = line.strip().split('\t')
            if len(cols) < 4:
                continue  # Ignorer les lignes mal formées

            cid = cols[0]  # CID1xxxxxxxx
            atc_code = cols[3]  # Code ATC
            
            # Si l'ID correspond à un CID valide
            if cid_pattern.match(cid):
                cid_to_atc[cid] = atc_code

    return cid_to_atc

def obtenir_atc_pour_cid(cid, cid_to_atc):
    """
    Renvoie le code ATC associé à un CID donné.
    
    Args:
        cid (str): Le code CID à rechercher.
        cid_to_atc (dict): Dictionnaire contenant les associations CID à ATC.
    
    Returns:
        str: Le code ATC associé au CID, ou un message d'erreur si non trouvé.
    """
    atc_code = cid_to_atc.get(cid)
    if atc_code:
        return atc_code
    else:
        return f"Aucun code ATC trouvé pour le CID {cid}"

# Exemple d'utilisation
cid_to_atc_file = "STITCH - ATC/chemical.sources.v5.0.tsv"  # Remplace par le chemin vers ton fichier CID-ATC
cid = "CID100104758"  # Remplace par le CID pour lequel tu veux trouver le code ATC

# Charger les associations CID-ATC depuis un fichier
cid_to_atc = charger_association_cid_atc(cid_to_atc_file)

# Obtenir le code ATC pour un CID donné
atc = obtenir_atc_pour_cid(cid, cid_to_atc)
print(f"Le code ATC associé à {cid} est : {atc}")
