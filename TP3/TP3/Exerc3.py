"""""
Exercice 3: Fusion de Listes et Dictionnaires
Créez deux listes noms et ages contenant des noms et des âges
respectivement.
Créez un dictionnaire appelé personnes en associant chaque nom à son âge
correspondant.
Affichez le dictionnaire personnes.
Ajoutez une nouvelle personne au dictionnaire en utilisant une saisie
utilisateur pour le nom et l'âge.
Affichez à nouveau le dictionnaire personnes après l'ajout.
"""""

age = [22, 20, 23, 19]
nom = ["Felix", "Emilya", "Isaac", "Remi"]

personne = {}

personne = dict(zip(nom,age))
print(personne)
print(dict(personne))
while(True):
    try:
        newName = str(input(print("Inserez nouveau nom : ")))
        newAge = int(input(print("Inserez nouvel age : ")))
        personne[newName] = newAge
        break
    except ValueError:
        print("Veuillez entre une entre valide")

personne[newName] = newAge

print(personne)