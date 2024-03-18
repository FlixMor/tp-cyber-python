#FelixM

lundi = "lundi"
mardi = "mardi"
mercredi = "mercredi"
jeudi = "jeudi"
vendredi = "vendredi"
samedi = "samedi"
dimanche = "dimanche"

jan = "janvier"
fev = "fevrier"
mar = "mars"
avr = "avril"
mai = "mai"
jun = "juin"
jul = "juillet"
aou = "aout"
sep = "septembre"
oct = "octobre"
nov = "novembre"
dec = "decembre"


jourSemaine = [lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche]

for i in jourSemaine:
    print(i)

print("Partie 2")
mois = (jan, fev, mar, avr, mai, jun, jul, aou, sep, oct, nov, dec)

x = 0
while(x < len(mois)):
    print(mois[x])
    x = x + 1

capitales = {
    "France" : "Paris",
    "Italie" : "Rome",
    "Allemagne" : "Berlin"}

#capitales["Canada"] = "Ottawa"

for pays, capitales in capitales.items():
    print("Capitale de ", pays, "est", capitales)