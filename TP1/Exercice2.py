#FelixM

age = 0
majeur = 18

while(age <= 0):
    age = int(input('Quelle est votre age ?'))
    if(age <= 0):
            print('Age Invalide Reesayer')
    if(age >= majeur):
        print('Vous etes majeur !')
    if(age < majeur):
        print('Vous etes mineur')