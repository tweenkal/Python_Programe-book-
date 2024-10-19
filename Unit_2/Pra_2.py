#👉Create a programe to retrive , display and update only a range of
#   elements from an array using indexing and slicing in array

import array as arr

a = arr.array('i',[1,2,3,4,5])

#Display array

print(a)

#Update array using indexing

a[0] = 7
print(a)

#Update array using slicing

a[0 : 2] = arr.array('i',[8,9])
print(a)


#output:-
# array('i', [1, 2, 3, 4, 5])
# array('i', [7, 2, 3, 4, 5])
# array('i', [8, 9, 3, 4, 5])