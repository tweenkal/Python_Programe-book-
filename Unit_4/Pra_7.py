from mmap import error

import  mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Twinkal@123",
        database="Twinkal1"
    )

    if mydb is None:
        print("Database is not connected")

    else:
        print("Database is connected")

    cursor = mydb.cursor()
    cursor.execute("Create table employee33(id int(10) primary key,name varchar(10),sal numeric(10))")
    print("Employee table is created")
    cursor = mydb.cursor()
    cursor.execute("insert into employee33 values('1','Twinkal','20000')")
    cursor.execute("insert into employee33 values('2','Hinal','19000')")
    cursor.execute("insert into employee33 values('3','sejal','18000')")
    print("new table is created")
    mydb.commit()
    cursor.execute("select * from employee33")
    rows = cursor.fetchall()
    print(rows)

    for i in rows:
        print(i)

    mydb.commit()

except error as e:
    print(e)

