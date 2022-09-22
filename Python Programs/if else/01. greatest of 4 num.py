# find greatest of four numbers

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if a>b:
    f1 = a
else:
    f1 = b
if c>d:
    f2 = c
else:
    f2 = d
    
if f1>f2:
    print(f"{f1} is greatest")
else:
    print(f"{f2} is greatest")