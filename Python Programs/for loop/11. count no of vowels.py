vowel = 'aeiou'
str = input("Enter a string: ").lower()
count = 0

for i in str:
    if i in vowel:
        count += 1
print(count)