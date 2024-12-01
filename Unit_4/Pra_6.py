from dbm import error

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "Twinkal@123",
)

print(mydb)

try:
    cursor = mydb.cursor()
    cursor.execute("Create Database Sample_Db12")
    cursor.execute("Show Databases")
    my = cursor.fetchall()
    print("Database is created")

    for i in my:
        print(i)

except error as e:
    print(e)


