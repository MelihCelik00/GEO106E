A_519 = [[1,2,3],[4,5,6],[7,8,9]]
t_519 = [[0,0,0],[0,0,0],[0,0,0]]

for i_519 in range(len(A_519)):
    for j_519 in range(len(A_519[0])):
        t_519[j_519][i_519] = A_519[i_519][j_519]
for r_519 in t_519:
    print(r_519)
