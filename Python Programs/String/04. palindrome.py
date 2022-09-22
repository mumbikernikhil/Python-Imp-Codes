a = input("Enter a string: ").lower()

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")