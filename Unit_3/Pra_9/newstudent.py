from student import student

s = student()
s.setid(100)
s.setname("Twinkal")
s.setaddress("Uttamnagar")
s.setmarks(90)

print("Student Id=",s.getid())
print("Student Name=",s.getname())
print("Student adreess=",s.getaddress())
print("Student marks=",s.getmarks())

#output:-
# Student Id= 100
# Student Name= Twinkal
# Student adreess= Uttamnagar
# Student marks= 90