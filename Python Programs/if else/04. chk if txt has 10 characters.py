# check if entered string has 10 characters

a = input("Enter a word: ")

if len(a) > 10:
    print("More than 10 characters")
elif len(a) == 10:
    print("10 characters")
else:
    print("Less than 10 characters")