# 👉Create a decorater function to increase the value of a
#   function by 3.

def plus_one(number):
    def add_one(number):
        return number + 3

    result = add_one(number)
    return  result


# 👉Output:-
