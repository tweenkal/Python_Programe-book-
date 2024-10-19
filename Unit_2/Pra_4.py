
# 👉Write a programe to sort the array elements using bubble sort
#   technique.

arr = [11,23,24,53,56,22]

for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)

#output:-
# [11, 22, 23, 24, 53, 56]