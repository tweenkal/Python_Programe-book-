#👉Write a programe to understand the order of execution of methods in
#   several base classes according to method resolution order(MRO)

class A(object):
    def method(self):
        print("A class method")
        super().method()


class B(object):
    def method(self):
        print("B class method")
        super().method()

class C(object):
    def method(self):
        print("C class method")
        super().method()

class X(A,B):
    def method(self):
        print("X class method")
        super().method()

class Y(B,C):
    def method(self):
        print("Y class method")
        super().method()

class P(X,Y,C):
    def method(self):
        print("P class method")
        super().method()

newp = P()
print(P.mro())
newp.method()


#output:-
# [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
# P class method
# X class method
# A class method
# Y class method
# B class method
# C class method

