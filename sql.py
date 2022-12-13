"""
Commencez par lancer le logiciel XAMPP et START apache et mysql
puis sur un navigateur taper URL: http://localhost/phpmyadmin/
"""

import csv
import mysql.connector

#connection à Mysql****************************
mysqlconnect=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
)

mycursor=mysqlconnect.cursor()
mycursor.execute("DROP DATABASE IF exists CINEMA")
print("efface database")
mycursor.execute("CREATE DATABASE CINEMA")
print("Création de la base")
# sur phpmyAdmin dans l'onglet Bases de données vous pouvez observer la table nsi_table

#Maintenant que nous avons créer la base NSI_Table, nous pouvons nous connecter.
mysqlconnect=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="CINEMA"
   )
mycursor=mysqlconnect.cursor()

with open("./TP-SQL.sql") as f:
    lines = f.readlines()

for line in lines:
    if line != "\n":
        mycursor.execute(line)

mycursor.execute("""
SELECT titre 
FROM film
JOIN projection AS p
ON p.num_film = film.num_film
WHERE 
""")


# la méthode fetchall stock toute la base dans la variable answer
answer = mycursor.fetchall()
# Affichage de la base
for data in answer:
    print(data)


#déconnection à mysql
mysqlconnect.close()