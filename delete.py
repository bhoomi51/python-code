import mysql.connector

def Demo():
    database=mysql.connector.connect(
        host='localhost',
        database='fOOd',
        user='root',
        password='root@1234'
    )

    Cursor=database.cursor()
    statement="delete from food_info where f_name='CHEESE'"  #column name are also case-insensitive
    Cursor.execute(statement)
    print(Cursor.rowcount,"details are deleted...")
    database.commit()

Demo()