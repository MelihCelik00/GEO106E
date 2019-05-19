import os
file_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/names.txt","r+")
content_519 = file_519.read()
names_519 = content_519.split()
names_519

for name_519 in names_519:
    print(name_519)

file_519.close()