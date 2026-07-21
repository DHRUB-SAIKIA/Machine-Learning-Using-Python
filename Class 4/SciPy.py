import numpy as np
from SciPy import sparse

eye = np.eye(5)
print("NumPy array:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)

print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))