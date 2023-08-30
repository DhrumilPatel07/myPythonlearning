import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="hanuman.",
        database="mydatabase"
        )

cur = mydb.cursor()
s = " UPDATE books SET price = price + 10 WHERE price>300"
cur.execute(s)
mydb.commit()