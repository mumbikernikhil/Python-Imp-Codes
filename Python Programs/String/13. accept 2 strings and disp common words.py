s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")
x = s1.split()
y = s2.split()
for i in x:
    if i in y:
        print(i)