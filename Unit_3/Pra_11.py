# 👉write a programe to override super class comstructor and method
#   in sub class
from gettext import textdomain


class parent:
    def __init__(self,txt):
        self.message = txt

    def printmessage(self):
        print(self.message)
        print("From parent class")

class child(parent):
    def __init__(self,txt):
        super().__init__(txt)

    def printmessage(self):
        super().printmessage()
        print("From child class")

x = child("Hello ,and welcome!")
x.printmessage()


#output:-
# Hello ,and welcome!
# From parent class
# From child class
