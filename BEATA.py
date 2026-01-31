# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs

import random # on va surtout l'utiliser pour l'IA

##variables necessaires##
grille_debut = [    [2, 2, 2, 2, 2, 2, 2, 2, 2],  
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],  
                    [2, 2, 2, 2, 2, 2, 2, 2, 2],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],  
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],  
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],] #1 : les blancs; 2 : les noirs; 0 : espace vide

grille_milieu = [   [0, 2, 0, 2, 2, 0, 1, 2, 0], 
                    [1, 0, 0, 2, 1, 2, 0, 2, 2],  
                    [0, 0, 1, 0, 0, 0, 2, 0, 0],  
                    [1, 0, 2, 0, 1, 0, 0, 0, 1],  
                    [0, 1, 0, 0, 0, 0, 2, 0, 0],  
                    [0, 0, 0, 2, 0, 2, 0, 0, 0],  
                    [0, 2, 1, 1, 0, 0, 0, 1, 0],  
                    [2, 0, 1, 2, 1, 2, 0, 1, 2],  
                    [1, 2, 0, 0, 1, 1, 0, 2, 0],]

grille_fin = [  [0, 0, 0, 0, 0, 0, 2, 0, 0],  
                [1, 2, 0, 0, 0, 1, 0, 0, 1],  
                [0, 0, 0, 0, 2, 0, 0, 2, 0],  
                [0, 2, 0, 0, 0, 0, 0, 0, 0],  
                [1, 0, 0, 1, 0, 0, 2, 0, 0],  
                [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                [0, 0, 0, 1, 0, 1, 0, 0, 2],  
                [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                [0, 0, 0, 0, 0, 0, 0, 0, 0],]

grille_terminé = [  [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [1, 2, 0, 0, 0, 1, 0, 0, 1],  
                    [0, 0, 0, 0, 2, 0, 0, 2, 0],  
                    [0, 2, 0, 0, 0, 0, 0, 0, 0],  
                    [1, 0, 0, 1, 0, 0, 2, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 1, 0, 1, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],]

blanc = "○" # ces deux variables ne sont pas vraiment utilisées dans le code, elles sont juste 
noir = "●" # pour vous informer que quels pions sont blancs et lesquels sont noirs

lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
nombres = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]




##fonctions de saisis et d'affichages
def afficher_grille(grille):
    print("   1   2   3   4   5   6   7   8   9")
    for i in range(9):
        print(lettres[i], end=" ")
        for j in range(9):
            if grille[i][j] == 2:
                print("[●]", end=" ")
            elif grille[i][j] == 1:
                print("[○]", end=" ")
            else:
                print("[ ]", end=" ")
        print()
    return "BEATA"

def saisi_blanc():
    print("entrez les coordonnées d'un pion blanc")
    print("entrez : une lettre majuscule entre A et I, suivi immédiatement d'un chiffre entre 1 et 9 ")
    position = str(input("votre saisi : "))
    return position

def saisi_noir():
    print("entrez les coordonnées d'un pion noir")
    print("entrez : une lettre majuscule entre A et I, suivi immédiatement d'un chiffre entre 1 et 9 ")
    position = str(input("votre saisi : "))
    return position

def menu():
    print("!!!COUCOU!!!")
    print("vous jouez à *** BEATA ***")
    print("\n")
    print("choisissez votre type de jeu")
    print("\n")
    print("pour faire un jeu de 'joueur vs joueur', tapez 'a'")
    print("pour faire un jeu de 'joueur vs ordinateur', tapez 'b'")
    type_jeu = str(input("type de jeu choisi : "))
    while (type_jeu != 'a') and (type_jeu != 'b'):
        print("tapez 'a' pour joueur vs joueur, ou 'b' pour joueur vs ordinateur")
        type_jeu = str(input("type de jeu choisi : "))
    print("\n")
    print("maintenant, choisissez la grille dans laquelle vous voulez jouer")
    print("\n")
    print("pour jouer dans la grille 'debut', tapez '1'")
    print("pour jouer dans la grille 'milieu', tapez '2'")
    print("pour jouer dans la grille 'fin', tapez '3'")
    print("pour jouer dans la grille 'vraiment fin', tapez '4'")
    type_grille = str(input("type de grille choisi : "))
    while (type_grille != '1') and (type_grille != '2') and (type_grille != '3') and (type_grille != '4'):
        print("grille debut : '1' , grille milieu : '2' , grille fin : '3', grille vraiment fin : '4'")
        type_grille = str(input("type de grille choisi : "))
    print("OKKKKKKK")
    print("commençons le jeu MAINTENANT")
    print('\n')
    return type_jeu, type_grille


def type_mvt():
    #vous aller choisir un type de mouvement/prise avec cette focntion
    print("choisissez le type de mouvement que vous voulez faire")
    print("pour faire un prise par élimination, tapez 'e'")
    print("pour faire un prise de retournement, tapez 'r'")
    type_prise = str(input("le mouvement choisi : "))
    while(type_prise != 'e') and (type_prise != 'r'):
        print("élimination : 'e'")
        print("retournement : 'r'")
        type_prise = str(input("le mouvement choisi : "))
    print('\n')
    return type_prise

##fonctions auxiliaires##

def position_aléatoire(): #produit une position aléatoire
    indice_lettre = random.randint(0, 8)
    lettre = lettres[indice_lettre] #choisir une lettre aléatoire entre A et I
    indice_nombre = random.randint(0, 8)
    nombre = nombres[indice_nombre] #choisir un nombre aléatoire entre 1 et 9
    resultat = lettre + nombre
    return resultat

def compteur_pion(grille):
    # compte le nombre de pions blanc et noirs restants
    nb_blancs = 0
    nb_noirs = 0
    for ligne in grille:
        for case in ligne:
            if case == 1:
                nb_blancs += 1
            elif case == 2:
                nb_noirs += 1
    return (nb_blancs, nb_noirs)

def conversion(saisi):
    # convertit la saisi du joueur en indices de la matrice
    i_saisi = lettres.index(saisi[0])
    j_saisi = nombres.index(saisi[1])
    return i_saisi, j_saisi


def positions_relatives(pos_initiale, pos_finale):
    # renvoie la position relative entre deux cases/pions
    indice_initiale = conversion(pos_initiale)
    iInitiale = indice_initiale[0]
    jInitiale  = indice_initiale[1]
    indice_finale = conversion(pos_finale)
    iFinale = indice_finale[0]
    jFinale = indice_finale[1]

    # même ligne ou même colonne
    if iInitiale == iFinale: #les deux pions sont dans la même ligne
        if jInitiale < jFinale: # le pion blanc est à gauche du pion noir
            return "horizontale : à gauche"
        if jInitiale > jFinale: # le pion blanc est à droit du pion noir
            return "horizontale : à droite"
        
    if jInitiale == jFinale: #les deux pions sont dans la même colonne
        if iInitiale < iFinale: # le pion blanc est au dessus du pion noir
            return "verticale : au dessus"
        if iInitiale > iFinale: # le pion blanc est en dessous du pion noir
            return "verticale : en dessous"
        
    # même diagonal
    if (iInitiale - jInitiale == iFinale - jFinale) : 
        if (iInitiale < iFinale) and (jInitiale < jFinale): # diagonale(position de pion blanc) : ↖️
            return "diagonale : en haut à gauche"
        if (iInitiale > iFinale) and (jInitiale > jFinale): # diagonale : ↘️
            return "diagonale : en bas à droite"
        
    if (iInitiale + jInitiale == iFinale + jFinale) : 
        if (iInitiale < iFinale) and (jInitiale > jFinale): # diagonale : ↗️
            return "diagonale : en haut à droite"
        if (iInitiale > iFinale) and (jInitiale < jFinale): #diagonale : ↙️
            return "diagonale : en bas à gauche"
        
    return False 
        #la position relative entre le pion blanc et le pion noir n'est ni verticale, ni horizontale, ni dogonale,
        #donc les position des deux pions sont inacceptables et doivent êtres changées.


def creer_etape(pos_initiale, pos_finale):
    #ces "etapes" sont utilisés pour avancer/décaler d'une ou de plusieurs cases
    ietape = 0
    jetape = 0
    
    if positions_relatives(pos_initiale, pos_finale) == "horizontale : à gauche":
        jetape = 1 #ex : pour aller de pos_initiale à pos_finale, il faut "ajouter"
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "horizontale : à droite":
        jetape = -1 #ex : pour aller de pos_initiale à pos_finale, il faut "soustraire"
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "verticale : au dessus":
        ietape = 1
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "verticale : en dessous":
        ietape = -1
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "diagonale : en haut à gauche":
        ietape = 1
        jetape = 1
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "diagonale : en bas à droite":
        ietape = -1
        jetape = -1
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "diagonale : en haut à droite":
        ietape = 1
        jetape = -1
        return (ietape, jetape)
    if positions_relatives(pos_initiale, pos_finale) == "diagonale : en bas à gauche":
        ietape = -1
        jetape = 1
        return (ietape, jetape)
    

def not_deux_fois_pareil(pos_initiale, pos_finale):
    # pour voir les deux cases/pions choisis sont les mêmes ou pas
    if pos_initiale != pos_finale:
        return True #si les deux saisis sont les mêmes, alors la fonction renvoie True
    else:
        return False


##fonctions de verifications##
def est_au_bon_format(saisi):
    # verifie le format d'une saisi
    if len(saisi) != 2:
        return False
    partie_lettre, partie_chiffre = saisi[0], saisi[1]
    #les fonctions isalpha() ans isdigit() verifient si une variable est une lettre ou un chiffre
    if not(partie_lettre.isalpha() and partie_chiffre.isdigit()):
        return False
    return True


def est_dans_grille(ligne, colonne):
    # verifie si la saisi est dans la grille ou pas
    partie_lettre = ligne
    partie_chiffre = colonne
    if (partie_lettre not in lettres):
        return False
    if partie_chiffre not in nombres:
        return False
    return True

# j'ai écrit deux fonctions de verification pour les positions initiales/finales pour faciliter la compréhension du code, sinon on peut utiliser qu'une seul fonction
def verifie_pos_initiale(pos_initiale, grille, joueur : int): 
    #verifie s'il existe bien un pion blanc/noir à pos_initiale
    indice_initiale = conversion(pos_initiale)
    if grille[indice_initiale[0]][indice_initiale[1]] != joueur:
        return False
    else:
        return True
    

def verifie_pos_finale(pos_finale, grille, adversaire : int):
    #verifie s'il existe bien un pion blanc/noir à pos_finale
    indice_finale = conversion(pos_finale)
    if grille[indice_finale[0]][indice_finale[1]] != adversaire:
        return False
    else:
        return True
    

def not_est_adjacent(pos_initiale, pos_finale):
    #verifie si deux cases/pions choisis sont adjacents ou pas 
    indice_initiale = conversion(pos_initiale)
    iInitiale = indice_initiale[0]
    jInitiale = indice_initiale[1]
    indice_finale = conversion(pos_finale)
    iFinale = indice_finale[0]
    jFinale = indice_finale[1]

    if abs(iInitiale - iFinale) > 1 or abs(jInitiale - jFinale) > 1:
        return True
    else:
        return False
    

def verifie_obstacles(pos_initiale, pos_finale, grille):
    # verifier s'il y a des pions entre les pions à pos_initiale et pos_finale
    indice_initiale = conversion(pos_initiale)
    iInitiale = indice_initiale[0]
    jInitiale = indice_initiale[1]
    indice_finale = conversion(pos_finale)
    iFinale = indice_finale[0]
    jFinale = indice_finale[1]

    # même ligne ou même colonne
    if positions_relatives(pos_initiale, pos_finale) == "horizontale : à gauche":
        for j in range(jInitiale + 1, jFinale):
            if grille[iInitiale][j] != 0:
                return False
    if positions_relatives(pos_initiale, pos_finale) == "horizontale : à droite":
        for j in range(jFinale + 1, jInitiale):
            if grille[iInitiale][j] != 0:
                return False
    if positions_relatives(pos_initiale, pos_finale) == "verticale : au dessus":
        for i in range(iInitiale + 1, iFinale):
            if grille[i][jInitiale] != 0:
                return False
    if positions_relatives(pos_initiale, pos_finale) == "verticale : en dessous":
        for i in range(iFinale + 1, iInitiale):
            if grille[i][jInitiale] != 0:
                return False
        
    # même diagonal
    if (iInitiale - jInitiale == iFinale - jFinale) or (iInitiale + jInitiale == iFinale + jFinale): 
        # digonal : ↘                                  #diagonal : ↙
        # Determiner la direction pour les "etapes" : du bas vers le haut ou du haut vers le bas
        ietape = 1 if iInitiale < iFinale else -1
        jetape = 1 if jInitiale < jFinale else -1
        #pour savoir s'il faut monter ou descendre

        i, j = iInitiale + ietape, jInitiale + jetape
        while i != iFinale and j != jFinale:
            if grille[i][j] != 0:
                return False
            i += ietape
            j += jetape
    if positions_relatives(pos_initiale, pos_finale) == False:
        return False 
        #ici, l'obstacle est le fait qu'on ne peut pas arriver à notre destination désiré avec les règles du jeu
    else:
        return True
    

def case_apres_vide(pos_initiale, pos_finale, grille):
    # pour vois si la case qui suit le pion est vide (ou existe)
    # attention : cela dépende des deux pions, blanc et noir
    indice_finale = conversion(pos_finale)
    iFinale = indice_finale[0]
    jFinale = indice_finale[1]
    ietape = creer_etape(pos_initiale, pos_finale)[0]
    jetape = creer_etape(pos_initiale, pos_finale)[1]
    #on utilise la focntion creer_etape pour trouver cette "case suivante"
    i = iFinale + ietape
    j = jFinale + jetape

    if (i >= 9) or (i < 0) or (j >= 9) or (j < 0):#si les indices sont invalide(trop grandes ou petites)
        return False
    if grille[i][j] != 0:
        return False
    if grille[i][j] == 0:
        return True
    

def est_fin_partie(grille):
    # verifie la terminaison d'une partie de jeu (!!! partie != tour !!!)
    nb_blanc = 0
    nb_noir = 0
    for i in range(9):
        for j in range(9): #rappel : c'est une grille/matrice 9*9
            if grille[i][j] == 1:
                nb_blanc += 1
            if grille[i][j] == 2:
                nb_noir += 1
    if nb_noir < 6:
        return "blanc : win, noir : loose"
    elif nb_blanc < 6:
        return "blanc : loose, noir : win"   
    else:
        return False

##fonctions de mouvements##
def prise_elimination(pos_initiale, pos_finale, grille, joueur : int, adversaire : int):
    # réalise une prise par elimination
    # le "joueur" st soit 1, soit 2. ça dépend le tour de jeu. idem pour adversaire

    if (est_au_bon_format(pos_initiale)) and (est_au_bon_format(pos_finale)):
        if (est_dans_grille(pos_initiale[0], pos_initiale[1])) and (est_dans_grille(pos_finale[0], pos_finale[1])):
            if verifie_pos_initiale(pos_initiale, grille, joueur):
                if verifie_pos_finale(pos_finale, grille, adversaire):
                    if not_deux_fois_pareil(pos_initiale, pos_finale):
                        if verifie_obstacles(pos_initiale, pos_finale, grille):
                            if not_est_adjacent(pos_initiale, pos_finale):
                                indice_initiale = conversion(pos_initiale)
                                iInitiale = indice_initiale[0]
                                jInitiale  = indice_initiale[1]
                                indice_finale = conversion(pos_finale)
                                iFinale = indice_finale[0]
                                jFinale = indice_finale[1]
                                grille[iInitiale][jInitiale] = 0
                                grille[iFinale][jFinale] = joueur
                                return True
                            else:
                                return "ERREUR : les pions sont adjacent"
                        else:
                            return "ERREUR : il y a des obstacles entre les deux pions choisis"
                    else:
                        return "ERREUR : les deux saisis ne doivent pas êtres pareil"
                else:
                    return "ERREUR : la deuxième position choisis doit contenir un pion de l'adversaire"
            else:
                return "ERREUR : la première position choisi doit être l'un de votre propre pions"
        else:
            return "ERREUR : votre saisi sort de la grille"
    else:
        return "ERREUR : votre saisi n'est pas au bon format"


def prise_retournement(pos_initiale, pos_finale, grille, joueur : int, adversaire : int):
    # réalise une prise par retournement

    #verifications très similaires à prise par élimination, mais pas les mêmes
    if (est_au_bon_format(pos_initiale)) and (est_au_bon_format(pos_finale)):
        if (est_dans_grille(pos_initiale[0], pos_initiale[1])) and (est_dans_grille(pos_finale[0], pos_finale[1])):
            if verifie_pos_initiale(pos_initiale, grille, joueur):
                if verifie_pos_finale(pos_finale, grille, adversaire):
                    if not_deux_fois_pareil(pos_initiale, pos_finale):
                        if verifie_obstacles(pos_initiale, pos_finale, grille):
                            if case_apres_vide(pos_initiale, pos_finale, grille):
                                indice_initiale = conversion(pos_initiale)
                                iInitiale = indice_initiale[0]
                                jInitiale  = indice_initiale[1]
                                indice_finale = conversion(pos_finale)
                                iFinale = indice_finale[0]
                                jFinale = indice_finale[1]
                                grille[iInitiale][jInitiale] = 0
                                grille[iFinale][jFinale] = joueur
                                ietape = creer_etape(pos_initiale, pos_finale)[0]
                                jetape = creer_etape(pos_initiale, pos_finale)[1]
                                grille[iFinale + ietape][jFinale + jetape] = joueur
                                return True
                            else:
                                return "ERREUR : soit la case suivant est occupé, soit elle sort de la grille"
                        else:
                            return "ERREUR : il y a des obstacles entre les deux pions choisis"
                    else:
                        return "ERREUR : les deux saisis ne doivent pas êtres pareil"
                else:
                    return "ERREUR : la deuxième position choisis doit contenir un pion de l'adversaire"
            else:
                return "ERREUR : la première position choisi doit être l'un de votre propre pions"
        else:
            return "ERREUR : votre saisi sort de la grille"
    else:
        return "ERREUR : votre saisi n'est pas au bon format"


def enchainement(pos_initiale, pos_finale, grille, joueur : int, adversaire : int):
    reponse = str(input("voulez vous faire un enchainement? Y pour oui et N pour non "))
    while (reponse != "Y") and (reponse != "N"):
        reponse = str(input("Y pour oui et N pour non "))
    if reponse == "N":
        afficher_grille(grille)
        return 
    if reponse == "Y":
        while True:
            afficher_grille(grille)
            ietape, jetape = creer_etape(pos_initiale, pos_finale)
            i2, j2 = conversion(pos_finale)
            i1 = i2 + ietape #on determine les coordonnées de la case après le pion "retourné", en utilisant pos_initiale et pos_finale
            j1 = j2 + jetape 
            pos_initiale_nouvelle = lettres[i1] + nombres[j1]
            print(f"nouvelle position initiale = {pos_initiale_nouvelle} ")
            print("entrez les coordonnées de l'un des pions de l'adversaire pour continuer l'enchainement ")
            if joueur == 1:
                pos_finale_nouvelle = saisi_noir() #on veut retourner un pion noir
            elif joueur == 2:
                pos_finale_nouvelle = saisi_blanc() #on veut retourner un pion blanc
            prise_r = prise_retournement(pos_initiale_nouvelle, pos_finale_nouvelle, grille, joueur, adversaire)
            while prise_r != True:
                erreur = prise_r
                print(erreur)
                quitter = str(input("Voulez vous arrêter l'enchaînement ? tapez 'Y' pour oui ou 'N' pour non "))
                while (quitter != 'Y') and (quitter != 'N'):
                    quitter = str(input("Voulez vous arrêter l'enchaînement ? tapez 'Y' pour oui ou 'N' pour non "))
                if quitter == 'Y':
                    return
                print(f"position initiale = {pos_initiale_nouvelle} ")
                print("entrez une nouvelle position finale: ")
                if joueur == 1:
                    pos_finale_nouvelle = saisi_noir()
                elif joueur == 2:
                    pos_finale_nouvelle = saisi_blanc()
                prise_r = prise_retournement(pos_initiale_nouvelle, pos_finale_nouvelle, grille, joueur, adversaire)
            pos_initiale = pos_initiale_nouvelle
            pos_finale = pos_finale_nouvelle
            afficher_grille(grille)
            nb = compteur_pion(grille)
            print(f"nombre de pions blanc : {nb[0]}")
            print(f"nombre de pions noir : {nb[1]}")
            reponse = input("voulez-vous continuer l'enchainement ? Y pour oui, N pour non ")
            while (reponse != "Y") and (reponse != "N"):
                reponse = input("Y pour oui, N pour non: ")
            if reponse == "N":
                break
        afficher_grille(grille)
        return


## tour de jeu ##
def alterner_tour_de_jeu(joueur : int):
    #on peut aussi utiliser cette fonction pour "adversaire"
    if joueur == 1:
        joueur = 2
    elif joueur == 2:
        joueur = 1
    return joueur


## IA stupide ##
def IA_random(grille): #l'IA joue toujours avec les pions noir
    list_blancs = [] #contient les positions des pions blanc sous form  de string (ex : "D4")
    list_noirs = [] #même chose mais pour les pions noir
    for i in range(9): #grille 9 * 9
        for j in range(9):
            if grille[i][j] == 1:
                position = lettres[i] + nombres[j] # rappel : on peut faire de la somme avec les string
                list_blancs.append(position)
            if grille[i][j] == 2:
                position = lettres[i] + nombres[j] 
                list_noirs.append(position)

    pairs = []
    for noir in list_noirs:
        for blanc in list_blancs:
            pairs.append((noir, blanc))
    random.shuffle(pairs)

    for depart, arrive in pairs:
        if prise_elimination(depart, arrive, grille, 2, 1) == True:
            print(f"{depart} a éliminé {arrive}")
            return True
        elif prise_retournement(depart, arrive, grille, 2, 1) == True:
            print(f"{depart} a retourné {arrive}")
            return True
    print("pas de mouvement possible pour l'IA pour l'instant :/")
    return True


## types de jeu ##

def jvj(grille, joueur : int, adversaire : int): #joueur vs joueur
    print("**JOUEUR VS JOUEUR**")
    while True:
        if joueur == 1:
            print("pions blanc : JOUEZ")
            mvt = type_mvt()
            if mvt == 'e':
                s1 = saisi_blanc()
                s2 = saisi_noir()
                prise = prise_elimination(s1, s2, grille, joueur, adversaire)
                while prise != True:
                    print(prise)
                    s1 = saisi_blanc()
                    s2 = saisi_noir()
                    prise = prise_elimination(s1, s2, grille, joueur, adversaire)
            if mvt == 'r':
                s1 = saisi_blanc()
                s2 = saisi_noir()
                prise = prise_retournement(s1, s2, grille, joueur, adversaire)
                while prise != True:
                    print(prise)
                    s1 = saisi_blanc()
                    s2 = saisi_noir()
                    prise = prise_retournement(s1, s2, grille, joueur, adversaire)
                afficher_grille(grille)
                enchainement(s1, s2, grille, joueur, adversaire)
            afficher_grille(grille)
            if est_fin_partie(grille) != False:
                return est_fin_partie(grille)

        if joueur == 2:
            print("pions noir : JOUEZ")
            mvt = type_mvt()
            if mvt == 'e':
                s1 = saisi_noir()
                s2 = saisi_blanc()
                prise = prise_elimination(s1, s2, grille, joueur, adversaire)
                while prise != True:
                    print(prise)
                    s1 = saisi_noir()
                    s2 = saisi_blanc()
                    prise = prise_elimination(s1, s2, grille, joueur, adversaire)
            if mvt == 'r':
                s1 = saisi_noir()
                s2 = saisi_blanc()
                prise = prise_retournement(s1, s2, grille, joueur, adversaire)
                while prise != True:
                    print(prise)
                    s1 = saisi_noir()
                    s2 = saisi_blanc()
                    prise = prise_retournement(s1, s2, grille, joueur, adversaire)
                afficher_grille(grille)
                enchainement(s1, s2, grille, joueur, adversaire)
            afficher_grille(grille)
            if est_fin_partie(grille) != False:
                return est_fin_partie(grille)
        joueur = alterner_tour_de_jeu(joueur)
        adversaire = alterner_tour_de_jeu(adversaire)



def jvo(grille): #joueur vs ordinateur
    print("**JOUEUR VS L'IA CONNE**")
    while True:
        # à vous de jouer
        print("vous avez les pions blanc")
        print("à vous : JOUEZ")
        mvt = type_mvt()
        if mvt == 'e':
            s1 = saisi_blanc()
            s2 = saisi_noir()
            prise = prise_elimination(s1, s2, grille, 1, 2)
            while prise != True:
                print(prise)
                s1 = saisi_blanc()
                s2 = saisi_noir()
                prise = prise_elimination(s1, s2, grille, 1, 2)
        if mvt == 'r':
            s1 = saisi_blanc()
            s2 = saisi_noir()
            prise = prise_retournement(s1, s2, grille, 1, 2)
            while prise != True:
                print(prise)
                s1 = saisi_blanc()
                s2 = saisi_noir()
                prise = prise_retournement(s1, s2, grille, 1, 2)
            enchainement(s1, s2, grille, 1, 2)
        if est_fin_partie(grille) != False:
            return est_fin_partie(grille)

        # à l'IA de jouer
        IA_random(grille)
        afficher_grille(grille)
        if est_fin_partie(grille) != False:
            return est_fin_partie(grille)



##fonctions de tests##

def test_compteur_pion():
    assert compteur_pion(grille_debut) == (27, 27)
    assert compteur_pion(grille_milieu) == (17, 20)
    return "passage du test"

def test_alterner_tour_de_jeu():
    assert alterner_tour_de_jeu(1) == 2
    assert alterner_tour_de_jeu(2) ==1
    return "passage du test"

def test_conversion(): 
    assert conversion("A8") == (0, 7)
    assert conversion("I9") == (8, 8)
    assert conversion("C3") == (2, 2)
    return "passage du test"

def test_position_relative():
    assert positions_relatives("I9", "A1") == "diagonale : en bas à droite"
    assert positions_relatives("A1", "I9") == "diagonale : en haut à gauche"
    assert positions_relatives("I9", "I9") == False
    assert positions_relatives("B6", "E4") == False
    assert positions_relatives("B6", "B8") == "horizontale : à gauche"
    assert positions_relatives("B8", "B6") == "horizontale : à droite"
    assert positions_relatives("D1", "C1") == "verticale : en dessous" 
    assert positions_relatives("C1", "D1") == "verticale : au dessus"
    assert positions_relatives("B7", "F3") == "diagonale : en haut à droite"
    assert positions_relatives("F3", "B7") == "diagonale : en bas à gauche"
    return "passage du test"

def test_creer_etape():
    assert creer_etape("A2","H9") == (1, 1)
    assert creer_etape("H9","A2") == (-1, -1)
    assert creer_etape("A3","H3") == (1, 0)
    assert creer_etape("H3","A3") == (-1, 0)
    assert creer_etape("E5","E6") == (0, 1)
    assert creer_etape("E6","E5") == (0, -1)
    assert creer_etape("E6","D7") == (-1, 1)
    assert creer_etape("D7","E6") == (1, -1)
    assert creer_etape("D1","E6") == None
    return "passage du test"

def test_not_deux_fois_pareil():
    assert not_deux_fois_pareil("B1", "D8") == True
    assert not_deux_fois_pareil("B1", "B1") == False
    return "passage du test"

def test_est_au_bon_format():
    assert est_au_bon_format("") == False
    assert est_au_bon_format("aBc4") == False
    assert est_au_bon_format("6") == False
    assert est_au_bon_format("AA") == False
    assert est_au_bon_format("33") == False
    assert est_au_bon_format("C4") == True
    assert est_au_bon_format("I9") == True
    assert est_au_bon_format("W0") == True
    assert est_au_bon_format("x86") == False
    return "passage du test"

def test_est_dans_grille():
    assert est_dans_grille("A","1") == True
    assert est_dans_grille("d","7") == False
    assert est_dans_grille("K","1") == False
    assert est_dans_grille("a","1") == False
    assert est_dans_grille("I","0") == False
    return "passage du test"

def test_verifie_pos_initiale():
    assert verifie_pos_initiale("A1", grille_debut, 1) == False
    assert verifie_pos_initiale("H5", grille_debut, 1) == True
    assert verifie_pos_initiale("D3", grille_debut, 1) == False
    return "passage du test"

def test_verifie_pos_finale():
    assert verifie_pos_finale("A1", grille_debut, 2) == True
    assert verifie_pos_finale("H5", grille_debut, 2) == False
    assert verifie_pos_finale("D3", grille_debut, 2) == False
    return "passage du test"

def test_not_est_adjacent():
    assert not_est_adjacent("C2", "C2") == False
    assert not_est_adjacent("C2", "F6") == True
    assert not_est_adjacent("F5", "F6") == False
    assert not_est_adjacent("F5", "F6") == False
    assert not_est_adjacent("D1", "D7") == True
    return "passage du test"

def test_verifie_obstacles():
    assert verifie_obstacles("B2", "B4", grille_debut) == False
    assert verifie_obstacles("C9", "G8", grille_debut) == False
    assert verifie_obstacles("C9", "G9", grille_debut) == True
    assert verifie_obstacles("A2", "C2", grille_milieu) == True
    assert verifie_obstacles("A2", "D2", grille_milieu) ==  True
    assert verifie_obstacles("H9", "I8", grille_milieu) == True
    return "passage du test"

def test_est_fin_partie():
    assert est_fin_partie(grille_debut) == False
    assert est_fin_partie(grille_debut) == False
    assert est_fin_partie(grille_fin) == False
    assert est_fin_partie(grille_terminé) == "blanc : win, noir : loose"
    return "passage du test"

def test_case_apres_vide():
    assert case_apres_vide("D6", "D8", grille_debut) == True
    assert case_apres_vide("C6", "C8", grille_debut) == False
    assert case_apres_vide("B8", "C8", grille_debut) == True
    assert case_apres_vide("F5", "G5", grille_debut) == False
    assert case_apres_vide("F5", "F7", grille_debut) == True
    return "passage du test"

def test_prise_elimination():
    #enlevez les "#" pour voir les effets de la fonction sur le tableau
    #print(afficher_grille(grille_debut))
    #assert prise_elimination("G7", "C7", grille_debut, 1, 2) == True
    #print(afficher_grille(grille_debut))
    assert prise_elimination("E1", "D2", grille_fin, 1, 2) == "ERREUR : les pions sont adjacent"
    assert prise_elimination("H6", "C1", grille_debut, 1, 2) == "ERREUR : il y a des obstacles entre les deux pions choisis"
    assert prise_elimination("G4", "E4", grille_debut, 1, 2) == "ERREUR : la deuxième position choisis doit contenir un pion de l'adversaire"
    return "passage du test"

def test_prise_retournement():
    #enlevez les "#" pour voir les effets de la fonction sur le tableau
    assert prise_retournement("G2", "C2", grille_debut, 1, 2) == "ERREUR : soit la case suivant est occupé, soit elle sort de la grille"
    #assert prise_retournement("C3", "D3", grille_milieu, 1, 2) == True
    assert prise_retournement("B1", "B6", grille_milieu, 1, 2) == "ERREUR : il y a des obstacles entre les deux pions choisis"
    return "passage du test"


##main##

def tests_générale():
    assert test_alterner_tour_de_jeu() == "passage du test"
    assert test_compteur_pion() == "passage du test"
    assert test_conversion() == "passage du test"
    assert test_case_apres_vide() == "passage du test"
    assert test_creer_etape() == "passage du test"
    assert test_not_deux_fois_pareil() == "passage du test"
    assert test_position_relative() == "passage du test"
    assert test_est_au_bon_format() == "passage du test"
    assert test_est_dans_grille() == "passage du test"
    assert test_verifie_pos_initiale() == "passage du test"
    assert test_verifie_pos_finale() == "passage du test"
    assert test_not_est_adjacent() == "passage du test"
    assert test_verifie_obstacles() == "passage du test"
    assert test_est_fin_partie() == "passage du test"
    assert test_case_apres_vide() == "passage du test"
    assert test_prise_elimination() == "passage du test"
    assert test_prise_retournement() == "passage du test"
    return "tous les tests sont passés :)"


def main():
    jeu, grille = menu()

    if grille == '1':
        grille = grille_debut # je redéfini la variable grille
    elif grille == '2':
        grille = grille_milieu
    elif grille == '3':
        grille = grille_fin
    elif grille == '4': # c'est juste une grille très proche de la fin
        grille = grille_terminé

    if jeu == 'a':
        afficher_grille(grille)
        print(jvj(grille, 1, 2))
    elif jeu == 'b':
        afficher_grille(grille)
        print(jvo(grille))
    
    return "FINITO"


##EXECUTION##

print(tests_générale())
print(main())