# 👉Write a programe to handle some built in execeptions
#   like zeroDivisionError.

a = int(input("Enter a dividend="))
b = int(input("Enter a divisior="))

try:
    ans = a / b

except ZeroDivisionError:
    print("zero division error")

else:
    print("Answer=",ans)

#output:-
# Enter a dividend=10
# Enter a divisior=0
# zero division error

# Enter a dividend=10
# Enter a divisior=1
# Answer= 10.0