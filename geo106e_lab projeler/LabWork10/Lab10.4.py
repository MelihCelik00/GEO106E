
def mult_matrices_519(matrix1_519,matrix2_519):
    row1_519, column1_519 = len(matrix1_519), len(matrix1_519[0])
    row2_519, column2_519 = len(matrix2_519), len(matrix2_519[0])
    
    if row2_519 != column1_519:
        print("Matrix dimensions do not match for multiplication!")
        return None
    
    else:
        multip_519 = [[0 for j_519 in range(column2_519)] for i_519 in range(row1_519)]
        for i_519 in range(row1_519):
            for j_519 in range(column2_519):
                for k_519 in range(column1_519):
                    multip_519[i_519][j_519] += (matrix1_519[i_519][k_519] * matrix2_519[k_519][j_519])
        return multip_519