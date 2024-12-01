import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Twinkal@123",
        database="emp"
    )

    if mydb is None:
        print("Database is not connected")

    else:
        print("Database is connected")

    cursor = mydb.cursor()

    id = int(input("Enter emp id="))
    sql = "delete from emp1 where id = %s"
    val = (id,)
    cursor.execute(sql,val)
    print("record deleted")

    mydb.commit()

except error:
    print(error)

