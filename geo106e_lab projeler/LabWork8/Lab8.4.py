import math
f_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/coordinates.txt","r")
lines_519 = f_519.readlines()

pid_519 = []
x_519 = [] 
y_519 = [] 
z_519 = [] 
for line_519 in lines_519:
    line_519 = line_519.split()
    pid_519.append(line_519[0])
    x_519.append(float(line_519[1]))
    y_519.append(float(line_519[2]))
    z_519.append(float(line_519[3]))    

print("PNo","X\t","Y\t","Z",sep="\t")

for i in range(len(pid_519)):
    print(format(pid_519[i],"s"),end="\t")
    print(format(x_519[i],".3f"),end="\t")
    print(format(y_519[i],".3f"),end="\t")
    print(format(z_519[i],".3f"),end="\t")

distance_519 = []
for i in range(len(pid_519)-1):
    s = math.sqrt((x_519[i+1]-x_519[i])**2 + (y_519[i+1]-y_519[i])**2)
    print("Distance between", pid_519[i], "and", pid_519[i+1],":",format(s,".3f"))
    distance_519.append(s)
    
pidFile_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/pid_519.txt","w")
xFile_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/xcoordinates_519.txt","w")
yFile_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/ycoordinates_519.txt","w")
hFile_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/heights.txt","w")
sFile_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/distances.txt","w")

for i in range(len(pid_519)):
    print(pid_519[i], file=pidFile_519)
    print(x_519[i], file=xFile_519)
    print(y_519[i], file=yFile_519)
    print(z_519[i], file=hFile_519)
    if i<len(distance_519):
        print(distance_519[i], file=sFile_519)
f_519.close()