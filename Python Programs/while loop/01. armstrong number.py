n = int(input("Enter a number: "))

x =len(str(n))
temp = n
sum = 0

while temp > 0:
    c = temp%10
    sum = sum + c**x
    temp = temp//10
if sum == n:
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")