import numpy as np

matrix1_519 = np.genfromtxt("matrix1.txt", skip_header=3)
matrix2_519 = np.genfromtxt("matrix2.txt", skip_header=3)
multp_519 = np.dot(matrix1_519,np.transpose(matrix2_519))
