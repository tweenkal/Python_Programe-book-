# 👉Write a programe to override the super class method in subclass.

import math
class square:
    def area(self,x):
        print("Area of square=",(x*x))

class circle:
    def area(self,x):
        print("Area of circle=",(math.pi * x * x))

c = circle()
c.area(4)

#output:-
# Area of circle=50.27