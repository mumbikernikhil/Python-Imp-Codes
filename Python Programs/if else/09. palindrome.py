a = input("Enter a word: ")
rev = a[::-1]

if a == rev:
    print("String is Palindrome")
else:
    print("Not Palindrome")