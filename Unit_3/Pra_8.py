# 👉Write a programe to create a Emp class and make all the members of
#   the Emp class available to another class(MyClass).[By passing members
#   of one class to another]

class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.salary = sal

    def display(self):
        print("Id=",self.id)
        print("Name=",self.name)
        print("salary=",self.salary)

class myclass:
    @staticmethod
    def mymethod(e):
        e.salary += 1000
        e.display()

e = Emp(1001 , "Raj Kumar" , 12000.75)
myclass.mymethod(e)


#output:-

# Id= 1001
# Name= Raj Kumar
# salary= 13000.75
