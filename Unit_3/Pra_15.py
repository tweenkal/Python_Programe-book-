# 👉Write a programe to check the object type to know whether the method
#   exists in the object or not.

class Dog:
    def talk(self):
        print("Bow Wow")

class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Hello , Hi")


def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()

    elif hasattr(obj,"bark"):
        obj.talk()

    else:
        print("Wrong object passed")


x = Duck()
call_talk(x)

x = Human()
call_talk(x)

x = Dog()
call_talk(x)


#output:-
# Quack Quack
# Hello , Hi
# Bow Wow