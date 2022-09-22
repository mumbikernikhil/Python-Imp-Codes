word = input("Enter a string: ")
vowels = "aeiou"
count = 0
for i in word:
    if i in vowels:
        count += 1
print(count)


# word = input("Enter a string: ")
# vowels = "aeiou"
# countA = 0
# countE = 0
# countI = 0
# countO = 0
# countU = 0

# for i in word:
#     if i == 'a':
#         countA += 1
#     if i == 'e':
#         countE += 1
#     if i == 'i':
#         countI += 1
#     if i == 'o':
#         countO += 1
#     if i == 'u':
#         countU += 1

# print(f"a:{countA}", end = " ")
# print(f"e:{countE}", end = " ")
# print(f"i:{countI}", end = " ")
# print(f"o:{countO}", end = " ")
# print(f"u:{countU}", end = " ")

# Eg: welcome
# o/p =  a:0  e:2  i:0  o:1  u:0 