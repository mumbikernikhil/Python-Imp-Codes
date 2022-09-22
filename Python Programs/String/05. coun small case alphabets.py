a = input("Enter a string: ")
count = 0

for i in a:
    if i.islower():
        count += 1
print("Total small case alphabets are:",count)
