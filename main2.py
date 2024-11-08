import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Biello_Database"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Animali_Domestici (nome, razza, eta, peso, colore) VALUES (%s, %s, %s, %s, %s)"

val = [
  ('Fido', 'Labrador', 3, 30,  'Marrone'),
  ('Micia', 'Persiano', 5, 4, 'Bianco e nero'),
  ('Rocky', 'Golden Retriever', 2, 28, 'Dorato'),
  ('Luna', 'Siamese', 4, 3, 'Grigio'),
  ('Leo', 'British Shorthair', 1, 6, 'Grigio blu'),
  ('Stella', 'Border Collie', 1, 18, 'Bianco e nero'),
  ('Max', 'Pastore tedesco', 6, 35, 'Nero e marrone'),
  ('Nina', 'Chihuahua', 2, 2, 'Marrone'),
  ('Charlie', 'Canarino', 1, 20, 'Giallo')
]



mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "i record sono stati inseriti")