import numpy as np

matrix1_519 = np.genfromtxt("matrix3.txt")
matrix_inv_519  = np.linalg.inv(matrix1_519)
unitMatrix_519 = np.dot(matrix1_519, matrix_inv_519)
print(unitMatrix_519)