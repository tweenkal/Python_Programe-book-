# 👉Write a programe to demonstarate the use of instance and
#   class/static variables.

class sample():
    var = 10        #class variable


#class method:

    @classmethod
    def new_modify(cls):
        cls.var += 1

s1 = sample()
s2 = sample()

print("X in s1=",s1.var)
print("X in s2=",s2.var)

s1.new_modify()
print("X in s1=",s1.var)
print("X in s2=",s2.var)

#output:-
# X in s1= 10
# X in s2= 10
# X in s1= 11
# X in s2= 11

#instance variable

class sample():
    def __init__(self):
        self.x = 10     #Instance variable

    #Instance method
    def modify(self):
        self.x += 1

s1 = sample()
s2 = sample()

print("X in s1=",s1.x)
print("Y in s2=",s2.x)

s1.modify()
print("X in s1=",s1.x)
print("X in s2=",s2.x)


#output:-
# X in s1= 10
# X in s2= 10
# X in s1= 11
# X in s2= 11