# 👉Write a programe to access the base class constructor from a sub
#   class by using super() method and also without using super() method.
from idlelib.autocomplete import completion_kwds


class square:
    def __init__(self,x):
        self.x = x

    def area(self):
        print("Aria of square:",self.x * self.x)

class rectangle(square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def area(self):
        super().area()
        print("Area of Rectangle=",self.x * self.y)

a , b =[float(x) for x in input("Enter length and breadth=").split()]
r = rectangle(a,b)
r.area()


#output:-
# Enter length and breadth=3 4
# Aria of square: 9.0
# Area of Rectangle= 12.0


