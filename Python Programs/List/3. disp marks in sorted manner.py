l1 = []

for i in range(1,7):
    ui = int(input(f"Enter marks of student{i}: "))
    l1.append(ui)
    l1.sort()

print(l1)