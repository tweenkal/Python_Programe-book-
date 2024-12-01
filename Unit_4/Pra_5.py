# 👉Write a programe to import detetime module and format the
#   date as rewuired.also use the same module to calculate the
#   difference between your birthday and today in days.

import datetime

year = int(input("Enter your birth year="))
month = int(input("Enter your birth month="))
day = int(input(("Enter your birth day=")))

today = datetime.date(year, month, day)
birthday = datetime.date.today()
Difference = today - birthday
print("Difference is",Difference.days,"days")
