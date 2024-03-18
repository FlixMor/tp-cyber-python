def produit(num1,num2):
    total = num1 * num2
    return total

total = 0
num1 = 1
num2 = 1

while(True):
    try:
        num1 = float(input("Entrez le Premier nombre: "))
        num2 = float(input("Entrez le Deuxieme nombre: "))
        break  
    except ValueError:
        print("Entrer un chiffre valide.")

total = produit(num1,num2)
print("Le produit est : ",total)