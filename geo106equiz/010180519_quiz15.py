"""
Melih Safa Çelik
ID: 010180519
(grad/200) = (radian/pi) = (Derece/180)
radius_519 = angle_degree_519*(math.pi / 180)
"""
import math

a = 6378137.0000
b = 6356752.3141
M_519 = (-2.5 * 180) / math.pi
E_519 = (-2.5 * 180) / math.pi

guess_519 = 0

ecentricity_519 = abs( ((a**2) - (b**2)) / (a**2) ) ** ( 1/2 )

while E_519 > ( 1 / 1000000000000 ):
    E_519 = M_519 + (ecentricity_519 * math.sin(E_519))
print(E_519)