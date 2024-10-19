# 👉Write a programe to create student class with a constructor
#   having more than one parameter.
import stat
import string

from django.contrib.admindocs.utils import named_group_matcher


class student:
    def __init__(self , nm='',ag = 20 , m=0):
        self.name = nm
        self.age = ag
        self.marks = m

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)

s = student("Twinkal",20,90)
s.display()

s1 = student("Twinkal")
s1.display()

#output:-
# Name: Twinkal
# Age: 20
# Marks: 90
# Name: Twinkal
# Age: 20
# Marks: 0