import mysql.connector
database = mysql.connector.connect(host='localhost',user='root',password='root@1234')
print(database)

Cursor=database.cursor()
Cursor.execute("CREATE DATABASE Food")

