# 👉Write a programe to demonstrate the use of positional argument ,
#   keyword argument and default argument.

#👉Position argumet

def positional(Hinal,Twinkal,Sejal):
    print(Hinal,Twinkal,Sejal)

a = 'Hinal'
b = 'Twinkal'
c = 'Sejal'

positional(a,b,c)

#output:-
# Hinal Twinkal Sejal

#👉Keyword argument

def keyword(Hinal,Twinkal,Sejal):
    print(Hinal,Twinkal,Sejal)

a = 'Hinal'
b = 'Twinkal'
c = 'Sejal'

keyword(Hinal=a , Twinkal=b , Sejal=c )

#output:-Hinal Twinkal Sejal

# 👉Default argument

def default(Hinal,Twinkal,Sejal = 'Sejal'):
    print(Hinal,Twinkal,Sejal)

a = 'Hinal'
b = 'Twinkal'
c = 'Sejal'

default(Hinal=a , Twinkal=b)

#output:-Hinal Twinkal Sejal