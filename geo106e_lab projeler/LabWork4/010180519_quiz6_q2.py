"""
Write a python script that allows
user to input two edges of a triangle
and the angle (in degrees) between
them to calculate the third edge of
a triangle using cosine theorem.
Outputs should have 4 decimal digits.
Here is an example output:
𝑐
2 = 𝑎
2 + 𝑏
2 − 2𝑎𝑏𝑐𝑜𝑠(𝛼)
"""

import math

a_519 = float(input("Enter 1st edge of triangle: "))
b_519 = float(input("Enter 2nd edge of triangle: "))
angle_degree_519 = float(input("Enter the angle between edges degrees: "))

radius_519 = angle_degree_519*(math.pi / 180)

c = ((a_519**2) + (b_519**2) - (2*a_519*b_519*(math.cos(radius_519))))** (1/2)

print("3rd edge of triangle: ",format(c,".4f"))