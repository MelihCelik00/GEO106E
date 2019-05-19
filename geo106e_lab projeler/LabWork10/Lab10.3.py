a1_519,b1_519,c1_519 = [float(x_519) for x_519 in input("Write inside of first row seperating with commas: ").split(",")]
a2_519,b2_519,c2_519 = [float(x_519) for x_519 in input("Write inside of second row seperating with commas: ").split(",")]
a3_519,b3_519,c3_519 = [float(x_519) for x_519 in input("Write inside of third row seperating with commas: ").split(",")]

X_519 = [[a1_519,b1_519,c1_519],[a2_519,b2_519,c2_519],[a3_519,b3_519,c3_519]]

d1_519,e1_519,f1_519 = [float(x_519) for x_519 in input("Write inside of first row seperating with commas: ").split(",")]
d2_519,e2_519,f2_519 = [float(x_519) for x_519 in input("Write inside of second row seperating with commas: ").split(",")]
d3_519,e3_519,f3_519 = [float(x_519) for x_519 in input("Write inside of third row seperating with commas: ").split(",")]

Y_519 = [[d1_519,e1_519,f1_519],[d2_519,e2_519,f2_519],[d3_519,e3_519,f3_519]]

result_519 = [[0,0,0],
              [0,0,0],
              [0,0,0]]
# iterate through rows
for i_519 in range(len(X_519)):
   # iterate through columns
   for j_519 in range(len(X_519[0])):
       result_519[i_519][j_519] = X_519[i_519][j_519] + Y_519[i_519][j_519]

for r_519 in result_519:
   print(r_519)