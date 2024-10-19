# 👉Write a programe tp convert the elements of two lists into
#   key values pairs of a dictionary.

keys = ['Cricket','Basketball','Hockey']
values = ['11','5','21']

combine_dict = dict(zip(keys,values))
print(combine_dict)


#output:-
# {'Cricket': '11', 'Basketball': '5', 'Hockey': '21'}