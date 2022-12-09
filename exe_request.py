import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

mycursor = conn.cursor()

with open('TP-SQL.sql') as f:
    requetes = f.readline()

for line in requetes:
    if line != "\n":
        mycursor.execute(line)