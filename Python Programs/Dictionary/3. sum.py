# sum of all items in a dictionary

dict = {'a':100, 'b':200, 'c':300}

# x = dict['a'] + dict['b'] + dict['c']
# print("Sum is", x)
sum = 0
for i in dict.values():
    sum += i
print("Sum is", sum)