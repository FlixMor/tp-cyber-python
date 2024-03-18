def est_pair(nombre):
    if nombre % 2 == 0:
        return True
    else:
        return False

while(True):
    try:
        nombre = int(input("Entrez le nombre a verifier: "))
        break
    except ValueError:
        print("Entre Invalide")

if est_pair(nombre) == True:
    print(f"Le nombre {nombre} est Pair !")
else:
    print(f"Le nombre {nombre} est Impair")