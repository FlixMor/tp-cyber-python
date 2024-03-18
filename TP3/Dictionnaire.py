def test():
    print("hello world")

ma_liste = [1,2,3,4,5,6,7,8,9,10]
mon_tuple = ()
dictionnaire = {
                'Lion':"Un mammifere",
                'Homme':"Etre humain",
                'Chat':"est un felin",
                1:"Devoir 1"               
                }
# Key : Valeur

#ajouter un element
dictionnaire["droite"] = "La droite"

#cree un dictionnaire
nombreDeRoue = {}
nombreDeRoue['voiture'] = 4
nombreDeRoue['velo'] = 2

#print entre 2 et 4    // :2   avant 2   3: apres 3
print(ma_liste[2:4])

print("----------------------------------------------")

#print definition de key
print(dictionnaire["droite"])

print("----------------------------------------------")


#print key
for element in dictionnaire:
    print(element)

print("----------------------------------------------")

#print index de element
for i in range(0,len(ma_liste)):
    print(f"Index={i} de lelement {ma_liste[i]}")

print("----------------------------------------------")

#parcourir les dict
for i in dictionnaire.items():
    print(i)
    
print("----------------------------------------------")
#print certaine partie de dictionnaire
for (key, value) in dictionnaire.items():
    print(f"{key} est un(e) {value}")

print("----------------------------------------------")