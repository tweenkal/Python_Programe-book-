# 👉Write a programe to create a list using range functions and
#   perform append,update and delete elements operations in it.

list = [i for i in range(0,9)]
print(list)

#output:-[0, 1, 2, 3, 4, 5, 6, 7, 8]

list.append(12)
print(list)

#output:-[0, 1, 2, 3, 4, 5, 6, 7, 8, 12]


#update
list.insert(1,14)
print(list)

#output:-[0, 14, 1, 2, 3, 4, 5, 6, 7, 8, 12]

#delet
list.remove(7)
print(list)

#output:-[0, 14, 1, 2, 3, 4, 5, 6, 8, 12]