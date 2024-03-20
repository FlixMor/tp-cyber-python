import mysql.connector as mysql
connexion = mysql.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "ecole"
)
requete = connexion.cursor()
test = requete.execute("SELECT * FROM ETUDIANT")
test = requete.fetchall()

for results in test:
    print(results)
