# Write a Python program to remove duplicates from a list

a = [10,20,30,20,10,50,60,40,80,50,40]

b = set()
for i in a:
    b.add(i)
print(b)