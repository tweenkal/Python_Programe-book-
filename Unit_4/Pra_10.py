from dbm import error

import mysql.connector


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Twinkal@123",
        database="emp",
    )

    if mydb is None:
        print("Database is not connected")

    else:
        print("Database is connected")

    cursor = mydb.cursor()

    id = int(input("Enter emp id="))
    inc = int(input("Enter inc ammount="))

    sql = "update emp1 set salary = salary + %s where id = %s"
    val = (inc , id ,)
    cursor.execute(sql , val)
    print("record updated")


    mydb.commit()

except error:
    print(error)
