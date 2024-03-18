
def sherlock(list):
    while True:
        try:
            nombre = float(input("Entrez le nombre a chercher: "))
            break
        except ValueError:
            print("Entre Invalide")

    if (nombre in list):
        return True
    else:
        return False
        #return valeur in list

def ajoutNombre(taille):# Remplir liste de nombre
    liste = []
    list.clear
    # Remplissage des elements de la liste
    for i in range(taille):
        while(True):
            try:
                print("Entrer la valeur du", i + 1, "nombre : ")
                # l'utilisateur entre une donner qui supporte les ,
                inputnombre = float(input())
                if(inputnombre > 0 ):
                    # Incere un element a la fin de la liste
                    liste.append(inputnombre)
                    break
                else:
                    print("Entre une valeur positive")
            except ValueError:
                print("Entre Invalide")
    return liste

def entrerTaille():                                         #Choisir une Taille
    taille = 0  # Initialisation
    while taille <= 0:  # Validation de input
        while True:
            try:
                print("Entrer la taille de la liste : ")
                taille = int(input())
                if(taille > 0):
                    break
                else:
                    print("Entre une taille valide")
                    continue
            except ValueError:
                print("Entre Invalide")
    return taille




print("SHERLOCK_LOOKUP")
print("")
taille = entrerTaille()
list = ajoutNombre(taille)
if sherlock(list):
    print(f"La valeur rechercher est presente dans la liste :{list} !")
else:
    print(f"Valeur Introuvable dans la liste :{list}")



