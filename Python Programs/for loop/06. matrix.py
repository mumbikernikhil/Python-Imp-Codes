a = int(input("Enter number of rows: "))
b = int(input("Enter number of coloumns: "))

matrix = []

for i in range(a):
    row = []
    for j in range(b):
        ui = int(input(f"Enter number at pocket {i} {j}: "))
        row.append(ui)
    matrix.append(row)

print(matrix)
## another way to print matrix

for i in range(a):
    for j in range(b):
        print(matrix[i][j], end = " ")
    print()