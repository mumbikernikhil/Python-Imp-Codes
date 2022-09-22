n = int(input("Enter a number: "))
sum = 0
while n%10 != 0:
    c = n%10
    sum = sum*10 + c
    n = n//10
print(f"Reverse of entered number is {sum}")