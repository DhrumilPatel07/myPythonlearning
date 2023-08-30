import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="hanuman.")

cur = mydb.cursor()

cur.execute("CREATE DATABASE mydatabase")