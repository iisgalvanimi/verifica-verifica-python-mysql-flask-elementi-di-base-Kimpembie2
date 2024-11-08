import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Biello_Database")
mycursor.execute("Use Biello_Database")
mycursor.execute("CREATE TABLE IF NOT EXISTS Animali_Domestici (id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(255), razza VARCHAR(255), eta INT, peso INT, colore VARCHAR(255))")