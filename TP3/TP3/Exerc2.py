"""""
Exercice 2: Manipulation de Dictionnaires
Créez un dictionnaire appelé personne avec les clés "nom", "âge" et "ville"
contenant vos propres informations.
Affichez la valeur associée à la clé "âge".
Modifiez la valeur associée à la clé "ville" pour "Paris".
Ajoutez une nouvelle paire clé-valeur au dictionnaire pour représenter le sexe
de la personne.
Supprimez la clé "ville" du dictionnaire.
Affichez le dictionnaire résultant.
"""""

personne  = {
    'nom':"Felix",
    'age':"22",
    'ville':"MontTremblant"
}

print(personne['age'])

personne['ville'] = "Paris"

personne['sexe'] = "Homme"

del personne['ville']

print(personne)