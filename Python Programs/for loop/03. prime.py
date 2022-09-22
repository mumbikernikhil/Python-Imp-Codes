num = int(input("Enter a number: "))

for i in range(2,num):
    if num%i == 0:
        print("Not Prime")
else:
    print("Prime")

# prime = True
# for i in range(2,num):
#     if num % i == 0:
#         prime = False
#         break

# if prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")