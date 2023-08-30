import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hanuman.",
    database="mydatabase"
    )

cur = mydb.cursor()
c = "INSERT INTO books (bookid, title, price) VALUES(%s, %s ,%s)"

# # input single value
# b1 = (1,'Mahabharat',345)
# cur.execute(c, b1)

# input multiple values
book = [(2, 'Python', 146), (3, 'java', 222), (4, 'php', 112)]

cur.executemany(c, book)
mydb.commit()

