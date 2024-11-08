import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Biello_Database"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Animali_Domestici (id, nome, razza, eta, peso, colore) VALUES (%s, %s, %s, %s, %s, %s)"

val = [
  (1, 'Fido', 'Labrador', 3, 30,  'Marrone'),
  (2, 'Micia', 'Persiano', 5, 4, 'Bianco e nero'),
  (3, 'Rocky', 'Golden Retriever', 2, 28, 'Dorato'),
  (4, 'Luna', 'Siamese', 4, 3, 'Grigio'),
  (5, 'Leo', 'British Shorthair', 1, 6, 'Grigio blu'),
  (6, 'Stella', 'Border Collie', 1, 18, 'Bianco e nero'),
  (7, 'Max', 'Pastore tedesco', 6, 35, 'Nero e marrone'),
  (8, 'Nina', 'Chihuahua', 2, 2, 'Marrone'),
  (9, 'Charlie', 'Canarino', 1, 20, 'Giallo')
]



mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "i record sono stati inseriti")