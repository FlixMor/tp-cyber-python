from math_functions import advanced as ad, basic as ba

while True:
    try:
        print("Entrer la premiere valeur a calculer la factorielle: ")
        num1 = int(input())
        
        break
    except ValueError:
        print("Veuillez reesayer")


print(f"Voici le resultat de la factorielle du nombre saisis: {ba.factorielle(num1)}")

while True:
    try:
        print("Entrer la premiere valeur: ")
        num1 = int(input())
        print("Entrer la deuxieme valeur: ")
        num2 = int(input())
        break
    except ValueError:
        print("Veuillez reesayer")

print(f"Voici le resultat du carre de {num1} avec {num2}: {ad.puissance(num1, num2)}")