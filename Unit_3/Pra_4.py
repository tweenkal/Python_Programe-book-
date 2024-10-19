# 👉Write a programe to store data into instance using mutator methods
#   and to retrive data from the instances using accessor methods.



class student:
    #mutator method
    def setname(self,name):
        self.name = name

    #accessor method
    def getname(self):
        return self.name

    def setmarks(self,marks):
        self.marks = marks

    def getmarks(self):
        return self.marks

n = int(input("How many student ?"))

i = 0
while(i < n):
    s = student()
    name = input("Enter name=")
    s.setname(name)
    marks = int(input("Enter marks="))
    s.setmarks(marks)
    print("HI",s.getname())
    print("Your Marks:",s.getmarks())

    i+=1
    print("------------------------------------------------")

#output:-

# How many student ?2
# Enter name=Twinkal
# Enter marks=90
# HI Twinkal
# Your Marks: 90
# ------------------------------------------------
# Enter name=Hinal
# Enter marks=89
# HI Hinal
# Your Marks: 89
# ------------------------------------------------

