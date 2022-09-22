a = input("Enter a string: ")
x = a.split()
l = []
for i in x:
    if i not in l:
        l.append(i)
for i in l:
    print("String with unique words is:",i, end = " ")



## Method 2
# s = set(x)
# for i in s:
#     print(i, end = " ")