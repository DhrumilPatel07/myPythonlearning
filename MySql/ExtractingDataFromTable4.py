import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hanuman.",
        database="mydatabase"
        )

cur = mydb.cursor()
s = "SELECT * from books"
cur.execute(s)
result = cur.fetchall() 

for rec in result:
    print(rec)