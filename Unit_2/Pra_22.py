# 👉Create a python functions to accept python functions as a
#   dictionary and display its elements.


def func(d):
    for key in d:
        print("key",key,"value",d[key])

D = {'a':1 , 'b':2 , 'c':3}

func(D)


#output:-
# key a value 1
# key b value 2
# key c value 3