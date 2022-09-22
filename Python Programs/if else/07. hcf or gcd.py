# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers 
# is the largest positive integer that perfectly divides the two given numbers.
# For example, the H.C.F of 12 and 14 is 2.

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

if x > y:
    smaller = y
else:
    smaller = x

for i in range(1, smaller+1):
    if x%i == 0 and y%i == 0:
        hcf = i
print("HCF is", hcf)