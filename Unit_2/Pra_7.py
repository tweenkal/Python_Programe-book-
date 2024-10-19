# 👉Write a programe that removes any repeated items from a list
#   so that each items appears at most once.for instance the
#   list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].

li = [1,2,2,1,4,3,5,3,4,6,7,7,5,4]

new = list(set(li))
print(new)

#output:-
# [1, 2, 3, 4, 5, 6, 7]