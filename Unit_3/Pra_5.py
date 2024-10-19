# 👉Write a programe to use class method to handle the common features
#   of all the instance of student class.

class student:
    marks = 90
    @classmethod
    def modify(cls,name):
        print("{} scored {} marks".format(name,cls.marks))

student.modify("Twinkal")
student.modify("Hinal")


#output:-
# Twinkal scored 90 marks
# Hinal scored 90 marks