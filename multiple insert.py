import mysql.connector

def Demo():
    database=mysql.connector.connect(
        host='localhost',
        database='Food',
        user='root',
        password='root@1234'
    )

    Cursor=database.cursor()

    que="INSERT INTO food_info (f_Name,f_Price) VALUES (%s,%s)"
    val=[("burger","56"),
         ("samosa","90"),
         ("puff","30"),
         ("vadapav","20")]

    Cursor.executemany(que,val)   #for multiple insert executemany() are used..
    print(Cursor.rowcount,"details are inserted...")

    que="SELECT * FROM food_info";
    Cursor.execute(que)
    result = Cursor.fetchall()
    for x in result:
        print(x)
    database.commit()    #without doing commit data will not updated in workbench.

Demo()