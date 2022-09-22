a = input("Enter a string: ")
x = a.split()
b = ""
max = 0
for i in x:
    if len(i) > max:
        b = i
        max = len(i)
print(f"Longest word is: {b}")