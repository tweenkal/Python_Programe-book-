#👉 Write a programe to understand various methods of array class
#   mentioned:append , insert , remove , pop , index , tolist and count.
from numpy.ma.core import array

list = [1,2,3,4,5,6,6,7]
list.append(10)         #output:-[1, 2, 3, 4, 5, 6, 6, 7, 10]
print(list)

list.insert(2,12)
print(list)             #output:-[1, 2, 12, 3, 4, 5, 6, 6, 7, 10]

list.remove(4)
print(list)             #output:-[1, 2, 12, 3, 5, 6, 6, 7, 10]


list.pop()
print(list)             #output:-[1, 2, 12, 3, 5, 6, 6, 7]

print(list.index(3))    #output:-3

print(list.count(6))    #output:-2

import numpy as np

arr = array([1,2,3,4,5,6])
print(arr.tolist())     #output:-[1, 2, 3, 4, 5, 6]
