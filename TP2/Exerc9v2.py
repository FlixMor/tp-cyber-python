def cree_liste():
    liste = []
    """
    while(True):
        try:
            print("Entrer la taille :")
            taille = int(input())
            if taille > 0:
                break
            else:
                print("La taille doit etre superieur a 0 !")
        except ValueError:
            print("Un caractere n'est pas une taille.")
    
    while(True):
        try:
            for i in range(taille):
                print(f"Entrer la valeur du {i+1}e nombre : ")
                element = int(input())
                liste.append(element)
            break
        except ValueError:
            print("Veuillez reesayer.")
    return liste
    """

    #Prend des entree utilisateur jusqua un signal de quitter
    while(True):
        try:
            print("Entrez une valeur pour la liste ou appuyer sur 'q' pour quitter.")
            element = input()       
            if element.lower() == 'q':
                break
            else:
                liste.append(int(element))           
        except ValueError:
            print("Erreur detecter")

    return liste


def tri_croissant(liste:list):
    liste = sorted(liste)
    return liste
     

liste = cree_liste()
liste = tri_croissant(liste)
print(liste)
