s = input("Enter a string: ")
x = s.split()
min = 100 
newStr = ""

for i in x:
    if len(i) < min:
        newStr = i
        min = len(i)
print("Smallest word in string is:", newStr)