# 👉Write a programe to handle multiple execeptions like
#   syntaxerror and typeerror.

try:
    a = eval(input("Enter a dividend="))
    b = eval(input("Enter a divisor="))

    ans = a / b

except (TypeError,SyntaxError):
    print("Error")

else:
    print("Answer=",ans)

#output:-
# Enter a dividend=10
# Enter a divisor=1
# Answer= 10.0

# Enter a dividend=10
# Enter a divisor=k
# Show the error
