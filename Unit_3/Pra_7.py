# 👉Create a bank class with two variables name and balance. Implement
#   a constructor to initialize the variables.also implement deposite
#   and withdeawles using instance methods.

import  sys

class bank(object):
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount
        return self.balance

    def withdrawals(self,amount):
        if amount > self.balance:
            print("Low balance,can not withdraw")

        else:
            self.balance -= amount
        return  self.balance

name = input("Enter name=")
b = bank(name)
while(True):
    print("d/D -deposite,w/W  - withdeawal , e/E  -exit")
    choice = input("Enter choice=")
    if choice == "e" or choice == "E":
        sys.exit()

    amount = float(input("Enter amount="))

    if choice == "d" or choice == "D":
        print("Balance after deposite=",b.deposite(amount))

    elif choice == "w" or choice == "W":
        print("Balance after withdeawles=",b.withdrawals(amount))
