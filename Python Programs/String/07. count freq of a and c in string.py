a = input("Enter a string: ")
countA = 0
countC = 0

for i in a:
    if i == 'a':
        countA += 1
    if i == 'c':
        countC += 1

print(f"a: {countA} | c: {countC}")