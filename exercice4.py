"""
TP2 – Exercice 4 : Gestion d’équipements techniques (Centre ORBIT-X)

Contexte :
Le centre ORBIT-X possède une salle d’équipements techniques organisée en grille 2D.
Chaque case peut contenir un équipement (machine, banc de test, simulateur),
ou être inutilisable.

Chaque équipement a :
- une CAPACITÉ (2 ou 4 personnes)
- un ÉTAT :
    - Disponible
    - Utilisé
    - En maintenance

Codes utilisés dans la grille :
- 'X'  : zone sans équipement
- 'D2' : équipement DISPONIBLE, capacité 2
- 'D4' : équipement DISPONIBLE, capacité 4
- 'U2' : équipement UTILISÉ, capacité 2
- 'U4' : équipement UTILISÉ, capacité 4
- 'M2' : équipement en MAINTENANCE, capacité 2
- 'M4' : équipement en MAINTENANCE, capacité 4

Objectifs :
1) Initialiser la grille
2) Affecter un équipement disponible
3) Trouver le meilleur équipement pour une équipe
4) Générer un rapport d’état global
"""

# ------------------------------------------------------------------
# Fonction fournie – NE PAS MODIFIER
# ------------------------------------------------------------------

def afficher_salle(salle):
    print("\n=== Salle d’équipements ===")
    print("   ", end="")
    for j in range(len(salle[0])):
        print(f" {j}", end="")
    print()
    for i, rangee in enumerate(salle):
        print(f"{i}: ", end="")
        for case in rangee:
            print(f" {case}", end="")
        print()
    print("=" * 30)


# ------------------------------------------------------------------
# 1) Initialisation de la grille
# ------------------------------------------------------------------

def initialiser_salle(nb_rangees, nb_colonnes, positions_equipements):
    """
    Initialise la salle d’équipements.

    Args:
        nb_rangees (int)
        nb_colonnes (int)
        positions_equipements (list):
            liste de tuples (rangee, colonne, capacite)
            capacite = 2 ou 4

    Returns:
        list: grille 2D remplie de 'X', 'D2' ou 'D4'
    """
    salle = []

    # TODO 1 :
    # Créer une grille nb_rangees × nb_colonnes remplie de 'X'
    salle = [["X" for _ in range(nb_colonnes)] for _ in range(nb_rangees)]
    # TODO 2 :
    # Pour chaque equipement (voir sa position) :
    #   - si capacite == 2, X -> 'D2'
    #   - si capacite == 4, X -> 'D4'
    for row, column, capacity in positions_equipements:
        if capacity == 2: salle[row][column] = "D2"
        elif capacity == 4: salle[row][column] = "D4"
    return salle

# -------------------------------------------------------------------
# 2) Affection des equipements
# -------------------------------------------------------------------


def affecter_equipement(salle, position):
    """
    Affecte un équipement DISPONIBLE.

    Args:
        salle (list): grille 2D
        position (tuple): (rangee, colonne)

    Returns:
        list: nouvelle grille (copie profonde)
            - 'D2' devient 'U2'
            - 'D4' devient 'U4'

    Règles :
    - Modifier uniquement si la case est 'D2' ou 'D4'
    - Sinon, ne rien faire
    """

    # TODO : Faire une copie de la salle et la nommer "nouvelle"
    nouvelle = [row.copy() for row in salle]

    # TODO :
    # Pour la position donnée :
    #      si nouvelle[r][c] == 'D2' -> 'U2'
    #      si nouvelle[r][c] == 'D4' -> 'U4'
    if nouvelle[position[0]][position[1]] == "D2": nouvelle[position[0]][position[1]] = "U2"
    elif nouvelle[position[0]][position[1]] == "D4": nouvelle[position[0]][position[1]] = "U4"
    return nouvelle


# -------------------------------------------------------------------
# 3) Calcul du score d'un equipement
# -------------------------------------------------------------------

def calculer_score_equipement(position, capacite, taille_equipe, nb_colonnes):
    """
    Calcule un score pour un équipement.

    Règles EXACTES :
    - Si capacite < taille_equipe : retourner -1
    - Base : 100 points
    - Pénalité : -10 par place inutilisée
        places_vides = capacite - taille_equipe
    - Bonus accès rapide : +20 si colonne == 0 ou colonne == nb_colonnes - 1
    - Bonus supervision : +5 si rangée < 3

    Args:
        position (tuple): (rangee, colonne)
        capacite (int): 2 ou 4
        taille_equipe (int)
        nb_colonnes (int)

    Returns:
        int: score ou -1
    """
    score = 0

    # TODO 1 : gérer le cas équipement trop petit
    # TODO 2 : score de base
    # TODO 3 : pénalité gaspillage
    # TODO 4 : bonus accès rapide
    # TODO 5 : bonus supervision
    if capacite < taille_equipe: return -1
    else:
        score = 100
        score -= 10*(capacite - taille_equipe)
        if position[1] == 0 or position[1] == nb_colonnes - 1: score += 20
        if position[0] < 3: score += 5
    return score

# -------------------------------------------------------------------
# 4) Recherche du meilleur equipement
# -------------------------------------------------------------------


def trouver_meilleur_equipement(salle, taille_equipe):
    """
    Trouve le meilleur équipement DISPONIBLE pour une équipe.

    Args:
        salle (list): grille 2D
        taille_equipe (int)

    Returns:
        tuple ou None :
            - ((rangee, colonne), capacite)
            - None si aucun équipement compatible

    Règles :
    - Considérer uniquement 'D2' et 'D4'
    - Score maximal
    - En cas d’égalité, conserver le premier rencontré
    """
    meilleur = None

    # TODO :
    # Parcourir la grille
    #   - si case == 'D2' ou 'D4'
    #       extraire capacite depuis la chaîne
    #       calculer le score
    #       comparer au meilleur
    temp_best = -1
    for row in range(len(salle)):
        for column in range(len(salle[row])):
            if salle[row][column] == "D2" or salle[row][column] == "D4":
                if calculer_score_equipement((row, column), int(salle[row][column][1]), taille_equipe, len(salle[row])) != -1 and calculer_score_equipement((row, column), int(salle[row][column][1]), taille_equipe, len(salle[row])) > temp_best:
                    temp_best = calculer_score_equipement((row, column), int(salle[row][column][1]), taille_equipe, len(salle[row]))
                    meilleur = ((row, column), int(salle[row][column][1]))

    return meilleur


# -------------------------------------------------------------------
# 5) Generation d'un rapport d'etat
# -------------------------------------------------------------------

def generer_rapport_etat(salle):
    """
    Génère un rapport global sur l’état des équipements.

    À compter :
    - disponibles 2 / 4
    - utilisés 2 / 4
    - maintenance 2 / 4

    Taux d’indisponibilité :
        (utilisés + maintenance) / total_equipements

    Returns:
        dict
    """
    rapport = {
        'disponibles_2': 0,
        'disponibles_4': 0,
        'utilises_2': 0,
        'utilises_4': 0,
        'maintenance_2': 0,
        'maintenance_4': 0,
        'taux_indisponibilite': 0.0
    }

    # TODO 1 : parcourir la grille et compter chaque type
    # TODO 2 : calculer le taux (gérer division par zéro)
    for row in salle:
        for cell in row:
            if cell == "D2": rapport["disponibles_2"] += 1
            elif cell == "D4": rapport["disponibles_4"] += 1
            elif cell == "U2": rapport["utilises_2"] += 1
            elif cell == "U4": rapport["utilises_4"] += 1
            elif cell == "M2": rapport["maintenance_2"] += 1
            elif cell == "M4": rapport["maintenance_4"] += 1
    total_equipment = rapport["maintenance_2"] + rapport["maintenance_4"] + rapport["utilises_2"] + rapport["utilises_4"] + rapport["disponibles_2"] + rapport["disponibles_4"]
    unavailable_equipment = rapport["maintenance_2"] + rapport["maintenance_4"] + rapport["utilises_2"] + rapport["utilises_4"]
    if total_equipment: rapport["taux_indisponibilite"] = unavailable_equipment/total_equipment
    return rapport

# -------------------------------------------------------------------
# TESTS main
# -------------------------------------------------------------------

if __name__ == "__main__":
    nb_rangees = 10
    nb_colonnes = 12

    # Positions : (rangée, colonne, capacité)
    # Mélange d'équipements 2 et 4, répartis dans la salle.
    positions = [
        # Rangée 0
        (0, 0, 2), (0, 2, 4), (0, 5, 2), (0, 11, 4),

        # Rangée 1
        (1, 1, 4), (1, 4, 2), (1, 7, 4), (1, 10, 2),

        # Rangée 2
        (2, 0, 4), (2, 3, 2), (2, 6, 2), (2, 9, 4),

        # Rangée 3
        (3, 2, 4), (3, 5, 2), (3, 8, 4), (3, 11, 2),

        # Rangée 4
        (4, 1, 2), (4, 4, 4), (4, 7, 2), (4, 10, 4),

        # Rangée 5
        (5, 0, 2), (5, 3, 4), (5, 6, 4), (5, 9, 2),

        # Rangée 6
        (6, 2, 2), (6, 5, 4), (6, 8, 2), (6, 11, 4),

        # Rangée 7
        (7, 1, 4), (7, 4, 2), (7, 7, 4), (7, 10, 2),

        # Rangée 8
        (8, 0, 2), (8, 3, 2), (8, 6, 4), (8, 9, 4),

        # Rangée 9
        (9, 2, 4), (9, 5, 2), (9, 8, 2), (9, 11, 4),
    ]

    print("=== PARTIE 1 : Initialisation (grande salle) ===")
    salle = initialiser_salle(nb_rangees, nb_colonnes, positions)
    afficher_salle(salle)

    print("\n=== Test affectations ===")
    # Affecter quelques équipements (on choisit des positions qui contiennent bien D2/D4)
    a_affecter = [(1, 1), (0, 11), (6, 11), (9, 2), (4, 4)]
    for pos in a_affecter:
        salle = affecter_equipement(salle, pos)

    # Essayer une case censée être 'X' (devrait ne rien changer)
    salle = affecter_equipement(salle, (0, 1))

    afficher_salle(salle)

    print("\n=== Ajout manuel de maintenances (pour tester le rapport) ===")
    # On force quelques maintenances sur des équipements encore disponibles si possible
    for (r, c) in [(0, 5), (5, 3), (7, 7)]:
        if salle[r][c] == 'D2':
            salle[r][c] = 'M2'
        elif salle[r][c] == 'D4':
            salle[r][c] = 'M4'

    afficher_salle(salle)

    print("\n=== PARTIE 2 : Scores (exemples) ===")
    print("Score (0,0) cap 2 équipe 2 :", calculer_score_equipement((0, 0), 2, 2, nb_colonnes))
    print("Score (0,2) cap 4 équipe 3 :", calculer_score_equipement((0, 2), 4, 3, nb_colonnes))
    print("Score (2,3) cap 2 équipe 3 (trop petit) :", calculer_score_equipement((2, 3), 2, 3, nb_colonnes))

    print("\n=== Meilleur équipement disponible ===")
    for taille in [1, 2, 3, 4, 5]:
        meilleur = trouver_meilleur_equipement(salle, taille)
        print(f"Équipe de {taille} -> {meilleur}")

    print("\n=== PARTIE 3 : Rapport d'état ===")
    rapport = generer_rapport_etat(salle)
    print(rapport)

    print("\n=== Test sur mini-grille (cas simple) ===")
    mini = [
        ['D2', 'U2', 'M4', 'X'],
        ['X',  'D4', 'X',  'U4']
    ]
    afficher_salle(mini)
    print("Rapport mini :", generer_rapport_etat(mini))


