#15. Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order



order =int(input("Enter the order of matrix: "))

matrix = []
print("Enter the elements with space between the elements")
for i in range(order):
    row = input(f"for Row {i+1}: ")
    row = row.split()
    row = [int(x) for x in row]
    matrix.append(row)

for row in matrix:
    print(row)

def rotc90(matrix):
    for j in range(len(matrix)):
        for k in range(j, len(matrix)):
            matrix[j][k], matrix[k][j] = matrix[k][j], matrix[j][k]

    for row in matrix:
        row.reverse()

    return matrix

matrix = rotc90(matrix)

for row in matrix:
    print(row)

#will do spiral traversal later

