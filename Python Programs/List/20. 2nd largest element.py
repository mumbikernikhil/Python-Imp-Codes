n = int(input("Enter the total elements you want in a list: "))

newList = []

for i in range(n):
    ui = int(input(f"Enter element at position {i}: "))
    newList.append(ui)
print("My List", newList)
newList.sort()

print("Smallest element in list is", min(newList))
print("2nd Largest element in list is", newList[-2])
print("Largest element in list is", max(newList))

# print("Largest element in list is", newList[-1])