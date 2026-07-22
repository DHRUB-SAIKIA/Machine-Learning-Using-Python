import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

print("Original Matrix:")
print(matrix)

new_matrix = matrix.reshape(2, 6)

print("\nReshaped Matrix:")
print(new_matrix)

# Number of elements
print("\nTotal Elements:", matrix.size)