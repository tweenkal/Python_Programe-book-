# 👉Write a programe to overload the addition operator(+) to make it
#   act on the class objects.
from django.views.defaults import page_not_found


class bookx:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages +  other.pages

class booky:
    def __init__(self,pages):
        self.pages = pages

b1 = bookx(100)
b2 = booky(110)
print("Total pages=",(b1 + b2))

#output:-
# Total pages= 210


