def tri_croissant(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

def entrerTaille():                                         
    taille = 0  # Initialisation
    while taille <= 0:  # Validation de input
        print("Entrer la taille de la liste : ")
        taille = int(input())
        if taille <= 0:
            print("Erreur détectée, veuillez réessayer.")
    return taille

def ajoutNombre(taille):                                    
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

ma_liste = []

taille = entrerTaille()
ma_liste = ajoutNombre(taille)
nouvelle_liste = tri_croissant(ma_liste)
print("Liste triée par ordre croissant :", nouvelle_liste)
