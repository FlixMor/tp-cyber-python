#FelixM

def calculer_moyenne(nombre):
    if not nombre:
        return 0
    #i = a + b + c + d + e + f
    somme = sum(nombre)
    moyenne = somme / len(nombre)
    return(moyenne)

a = int(input("Entrez une valeur pour la note 1,  "))
b = int(input("Entrez une valeur pour la note 2,  "))
c = int(input("Entrez une valeur pour la note 3,  "))
d = int(input("Entrez une valeur pour la note 4,  "))
e = int(input("Entrez une valeur pour la note 5,  "))
f = int(input("Entrez une valeur pour la note 6,  "))

list[a, b, c, d, e, f]
resultat = calculer_moyenne(list)
print("La moyenne est : ", resultat)