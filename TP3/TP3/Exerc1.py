"""
Exercice 1: Manipulation de Listes
Créez une liste appelée nombres contenant les entiers de 1 à 5.
Ajoutez les entiers de 6 à 10 à la fin de la liste.
Affichez la longueur de la liste.
Supprimez le nombre 3 de la liste.
Triez la liste dans l'ordre décroissant.
Affichez la liste résultante.
"""
def tri_decroissant(liste):
    n = len(liste)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if liste[j] < liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste


nombres = [1, 2, 3, 4, 5]
i = 6

while (i <= 10):
    nombres.append(i)
    i = i + 1

print(len(nombres))

nombres.pop() #Emleve la derniere valeur de la liste 
nombres.sort(reverse=True)
#tri_decroissant(nombres)

print(nombres)
