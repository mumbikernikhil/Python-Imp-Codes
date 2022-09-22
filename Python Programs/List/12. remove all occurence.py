#Remove all occurrences of a specific item from a list.
#write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]
lst2 = []

for i in list1:
    if i != 20:
        lst2.append(i)
print(lst2)


# while 20 in list1:
#     list1.remove(20)
# print(list1)