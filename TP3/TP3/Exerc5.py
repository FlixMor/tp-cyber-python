"""""
Exercice 5: Compréhension de Liste

Créez une liste appelée carrés contenant les carrés des nombres de 1 à 10
en utilisant une compréhension de liste.
Affichez la liste carrés.
"""""

liste = []
i = 1

while i <= 10:
    x = i * i
    liste.append(x)
    i = i + 1
print(liste)


carre = [x**2 for x in range(1, 11)]
print(carre)