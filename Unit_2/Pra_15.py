# 👉Write a programe to combine two list,perform repetation of
#   lists  and create cloning of lists.


list1 = [i for i in range(1,6)]
list2 = [i for i in range(7,11)]

print(list1)    #output:-[1, 2, 3, 4, 5]
print(list2)    #output:-[7, 8, 9, 10]


#combine two list
list3 = list1 + list2
print(list3)

#output:-[1, 2, 3, 4, 5, 7, 8, 9, 10]

#repeatation of list
new_list = [i for i in list3 for x in (0,1)]
print(new_list)

#output:-[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 7, 7, 8, 8, 9, 9, 10, 10]


#clonning of list
list_cloning = list3[:]
print(list_cloning)

#output:-[1, 2, 3, 4, 5, 7, 8, 9, 10]
