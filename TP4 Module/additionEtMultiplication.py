import operation as ope


while True:
    try:
        print("Entrer la premiere valeur: ")
        num1 = int(input())
        print("Entrer la deuxieme valeur: ")
        num2 = int(input())
        break
    except ValueError:
        print("Veuillez reesayer")

print("ADDITION")
print(ope.addition(num1, num2))
print("---------------------------")

while True:
    try:
        print("Entrer la premiere valeur: ")
        num1 = int(input())
        print("Entrer la deuxieme valeur: ")
        num2 = int(input())
        break
    except ValueError:
        print("Veuillez reesayer")

print("MULTIPLICATION")
print(ope.multiplication(num1, num2))
print("---------------------------")