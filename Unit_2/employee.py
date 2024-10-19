# 👉Create a programe name "employee.py" and implement the
#   functions DA,HRA,PF, and ITAX .create another prograne
#   that uses the function of employee module and calculate gross
#   and net salaries of an employee.

import  employee

print("salary programe")
name = str(input("Enter name of employee:"))
basic = float(input("Enter basic sallary:"))
netpay = employee.netPay(basic)
print(f'Net salary:{netpay}')
grosspay = employee.grossPay(basic,netpay)
print(f'grospay salary:{grosspay}')


