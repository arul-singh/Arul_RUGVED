import numpy as np

matrix = np.array([
    
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
print(matrix)
print(np.rot90(matrix, k=3))

#left to figure out spiral traversal