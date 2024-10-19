# 👉Write  a Programe to create a student class with name,age and
#   marks as data memebers .also create a method named display() to
#   view the students details.create an object to student class and call
#   the moethod using the oject .

class student:
    def __init__(self):
        self.name = "Twinkal"
        self.age = 20
        self.marks = 90

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)

s = student()
s.display()


#output:-

# Name: Twinkal
# Age: 20
# Marks: 90