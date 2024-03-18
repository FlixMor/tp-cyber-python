nombre = int(input('Écrivez un nombre entier positif : '))
nombre = int(nombre)

i = 2

while i < nombre and nombre % i != 0 :

    i = i + 1

if i == nombre :

    print('Le nombre', nombre, 'est premier !')

else :

    print(nombre,' nest pas un nombre premier.')