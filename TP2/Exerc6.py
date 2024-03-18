
# Fonctions Generale


def entrerTaille():                                         #Choisir une Taille
    taille = 0  # Initialisation
    while taille <= 0:  # Validation de input
        print("Entrer la taille de la liste : ")
        taille = int(input())
        if taille <= 0:
            print("Erreur détectée, veuillez réessayer.")
    return taille

def ajoutNombre(taille):                                    # Remplir liste de nombre
    liste = []
    list.clear
    # Remplissage des elements de la liste
    for i in range(taille):
        print("Entrer la valeur du", i + 1, "nombre : ")
        # l'utilisateur entre une donner qui supporte les ,
        inputnombre = float(input())
        # Incere un element a la fin de la liste
        liste.append(inputnombre)
    return liste

def calculerMoyenne(liste):                                 # Calculer la moyenne de la liste
    if len(liste) == 0:
        return 0
    moyenne = sum(liste) / len(liste)
    return moyenne

def menu(liste,taille):                                     # Fonction du Menu
    print("Entrer l'une des options suivante: ")
    print("1 - Choisir la taille de la liste")
    print("2 - Entrer des nombre dans la liste")
    print("3 - Calculer la moyenne")
    print("4 - Placer en ordre croissant")
    print("5 - Quitter")
    print("Voici la liste : ",liste)
    print("Taille : ",taille)
    choix = float(input())
    return choix

def tri_croissant(liste):                                   #Tri Croissant
    n = len(liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

# Debut du code

# Variable Globale
listeVide = []
liste = []
choix = 0
taille = 0
quitter = 5

# Ouverture du menu
while(choix != quitter):

    choix = menu(liste,taille)

    if choix == 1:      #Entrer la Taille de la liste
        taille = entrerTaille()  
        print("La taille de la liste est :", taille)

    elif choix == 2:    #Entrer des nombre dans la liste
        if taille > 0:
            liste = ajoutNombre(taille)
            print("Voici la liste : ",liste)
        elif taille <= 0:
            print("Erreur detecter *Taille Invalide*")

    elif choix == 3:    #Calculer la moyenne de la liste
        if liste != listeVide:
            moyenne = calculerMoyenne(liste)
            print("La moyenne de la liste :",liste," est : ", moyenne)
            print("")
        else:
            print("Erreur detecter *Liste Vide*")

    elif choix == 4:
        tri_croissant(liste)
        print("Tri coissant fait !")

    elif choix != quitter:    #Choix Invalide
        print("Choix de menu Invalide")