import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "Harsha989",
    passwd = "H@rsha989",
    database = "extractdata.py"
)

cursor = db.cursor()

## defining the Query
query = "SELECT id FROM creator"

cursor.execute(query)

## fetching all creators from the 'cursor' object
creators = cursor.fetchall()

for creator in creators:
    print(creator)