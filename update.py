import mysql.connector

def Demo():
    database=mysql.connector.connect(
        host='localhost',
        database='fOOd',
        user='root',
        password='root@1234'
    )

    Cursor=database.cursor()
    statement="UPDATE food_info SET f_Price=50 WHERE f_Name='CHEESE'"  #food_info and food_Info both are same and works..
    Cursor.execute(statement)
    print(Cursor.rowcount,"details are updated...")
    database.commit()

Demo()