import os
file_519 = open("/Users/melihsafacelik/Desktop/geomatik mühendisliği/geo106e/geo106e_lab projeler/LabWork8/numbers.txt","r+")
numbers_519 = file_519.read()
numbers_519 = numbers_519.split()

length_519 = len(numbers_519)

for i_519 in range(length_519):
    numbers_519[i_519] = int(numbers_519[i_519])

#numbers_519 = [int(numbers_519[i_519]) for i_519 in range(length_519)]

for i_519 in range(length_519):
    numbers_sqrd_519 = numbers_519[i_519]**2
    print(numbers_sqrd_519)

file_519.close()