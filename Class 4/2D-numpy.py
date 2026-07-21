# Create a 2D num py array with an digonal one, and zero's every were else:

import numpy as np

TwoDimentional = np.array([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
])

# arr = np.eye(5, dtype=int)
print(TwoDimentional)