import math

a_519 = float(input("Enter 1st edge of triangle: "))
b_519 = float(input("Enter 2nd edge of triangle: "))
angle_degree_519 = float(input("Enter the angle between edges in degrees: "))

radius_519 = angle_degree_519*(math.pi / 180)

area_519 = (1/2)*(a_519)*(b_519)*(math.sin(radius_519))


print("Area of the triangle: ",format(area_519,".4f"))