a = input("Enter a string: ").lower()
words = a.split()
words.sort()
for i in words:
    print(i)