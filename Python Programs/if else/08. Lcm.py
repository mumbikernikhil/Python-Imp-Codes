# The least common multiple (L.C.M.) of two numbers is the smallest positive integer 
# that is perfectly divisible by the two given numbers.
# For example, the L.C.M. of 12 and 14 is 84.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

maxNum = max(a,b)

while True:
    if (maxNum % a == 0) and (maxNum % b == 0):
        print(f"LCM of {a} and {b} is {maxNum}")
        break
    maxNum += 1