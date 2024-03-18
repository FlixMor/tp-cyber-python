"""""
Exercice 4: Recherche dans une Liste de Dictionnaires
Créez une liste de dictionnaires représentant des étudiants. Chaque
dictionnaire devrait avoir les clés "nom" et "note".
Affichez les noms des étudiants ayant obtenu une note supérieure ou égale à
10.
"""""

#etudiant = {'etu1':10,'etu2':15,'etu3':8,'etu4':5,'etu5':17}


def creeEtu():
    newName = str(input("Inserez nouveau nom : "))
    newNote = int(input("Inserez la note : "))
    etudiant[newName] = newNote

x = 1
etudiant = {}
while(x == 1):
    try:
        print("Entrer un  etudiant entrer - 1")
        print("Sinon entrer - 2")
        x = int(input())

        if x == 1:
            creeEtu()
        elif x == 2:
            break       
        else:
            print("Entrez Invalide")
    except ValueError:
        print("Veuillez entre une entre valide")

print(etudiant)

print("Voici la liste des etudiant avec une superieur a 10: ")
for (key, value) in etudiant.items():
    if(value >= 10):
        print(f"{key} a une note de {value}")
