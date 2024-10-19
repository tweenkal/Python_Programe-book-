# 👉Create a sample list of 7 elements and implement the list
#   methods mentioned:append,insert,copy,extend,count,remove,pop,sort,
#   reverese and clear.

list1 = [1,2,3,4,5,6,7,8]
print(list1)

#output:-[1, 2, 3, 4, 5, 6, 7, 8]

#append
list1.append(9)
print(list1)

#output:-[1, 2, 3, 4, 5, 6, 7, 8, 9]

#insert
list1.insert(2,5)
print(list1)

#output:-[1, 2, 5, 3, 4, 5, 6, 7, 8, 9]

#copy
list2 = list1.copy()
print(list2)

#output:-[1, 2, 5, 3, 4, 5, 6, 7, 8, 9]

#extend
another_list = ['A','B','C']
list1.extend(another_list)
print(list1)

#output:-[1, 2, 5, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C']

#count
print(list1.count(3))

#output:-1

#remove
list1.remove('C')
print(list1)

#output:-[1, 2, 5, 3, 4, 5, 6, 7, 8, 9, 'A', 'B']

#pop

print(list1.pop())

#output:-B

#sort

list2 = [4,7,5,2,4,5,7,8,9,5,3,2,4]
list2.sort()
print(list2)

#output:-[2, 2, 3, 4, 4, 4, 5, 5, 5, 7, 7, 8, 9]

#reverse

list1.reverse()
print(list1)

#output:-['A', 9, 8, 7, 6, 5, 4, 3, 5, 2, 1]

#clear

list2.clear()
print(list2)

#output:-[]
