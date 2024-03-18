def convertC(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

while(True):
    try:
        temp = int(input("Entrez la temperature en Fahrenheit: "))       
        break
    except ValueError:
        print("Entrer un chiffre valide.")

print("La temperature en Celsius est de : ",convertC(temp),"C")