import numpy as np



order =int(input("Enter the order of matrix: "))

matrix = []
print("Enter the elements with space between the elements")
for i in range(order):
    row = input(f"for Row {i}: ")
    row = row.split()
    row = [int(x) for x in row]
    matrix.append(row)

matrix = np.array(matrix)

rotated = np.rot90(matrix, k=3)
print(rotated)

#will do spiral traversal later

