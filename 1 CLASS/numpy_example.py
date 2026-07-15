#Load libary
import numpy as np

#Create 4X3 matrix
matrix = np.array([
    [1, 2,3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

#Reshape matrix into 2X6 matrix
reshaped_matrix = matrix.reshape(2, 6)

print(reshaped_matrix)