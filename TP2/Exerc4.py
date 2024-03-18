def pgcd(a, b):
    while b != 0:
        modulo = a % b         #modulo est le reste de la division entre a et b
        #a, b = b, modulo   
        a = b
        b = modulo
    return a


#a = int(input("Entrez le Premier nombre: "))
#b = int(input("Entrez le Deuxieme nombre: "))
while(True):
    try:
        resultat = pgcd(int(input("Entrez le Premier nombre: ")), int(input("Entrez le Deuxieme nombre: ")))
        break
    except ValueError:
        print("Entre invalide")

def pgcd2():
    while b:
        a, b = b, a % b
    return abs(a)