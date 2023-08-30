import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hanuman.",
        database="mydatabase"
        )

cur = mydb.cursor()
s = "DELETE FROM books WHERE title= 'php'"
cur.execute(s)
mydb.commit()