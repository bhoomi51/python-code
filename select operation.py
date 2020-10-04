import mysql.connector

def createTable():
    database=mysql.connector.connect(
        host='localhost',
        database='FOOD',    #in mysql tablenames and database are case-insensitive.
        user='root',
        password='root@1234'
    )

    Cursor=database.cursor()

    #tableName="CREATE TABLE food_info(f_Name VARCHAR(45),f_Price INT);"
    tableName="select * from food_info";
    Cursor.execute(tableName)

    result=Cursor.fetchall()

    for x in result:
        print(x)

createTable()