import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hanuman.",
    database="mydatabase"
    )

cur = mydb.cursor()
s = "CREATE TABLE books(bookid integer(4), title varchar(20), price float(5,2))"
cur.execute(s)

