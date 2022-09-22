# Write a Python program to print a specified list 
# after removing the 0th, 4th and 5th elements

lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new = []

# for index, item in enumerate (lst):
#     if index not in (0,4,5):
#         new.append(item)
# print(new)

lst = [x for (i,x) in enumerate(lst) if i not in (0,4,5)]
print(lst)