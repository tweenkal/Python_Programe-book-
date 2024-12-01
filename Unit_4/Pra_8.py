from mmap import error

import mysql.connector


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Twinkal@123",
        database="Twinkal1"
    )

    if mydb is None:
        print("database is not connected")

    else:
        print("DAtabase is connected")

    cursor = mydb.cursor()

    while('True'):
        choice = input("wouild you like to enter record")
        if(choice=="yes" or choice=="yes"):
            id = int(input("Enter emp id="))
            name = input("Enter emp name=")
            sal = int(input("Enter emp salary="))
            sql = "insert into employee33(id ,name,sal) values (%s,%s,%s)"
            val = (id,name,sal)

            cursor.execute(sql , val)
            mydb.commit()

        elif(choice == "no" or choice == "no"):
            break

        else:
            print("wrong input")

except error as e:
    print(e)



