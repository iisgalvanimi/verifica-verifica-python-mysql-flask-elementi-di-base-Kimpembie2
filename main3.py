import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Biello_Database"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Animali_Domestici")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)    