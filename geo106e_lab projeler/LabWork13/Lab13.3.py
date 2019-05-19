# -*- coding: utf-8 -*-
"""
Created on Tue May 08 14:12:43 2018

@author: isiler
"""

import math

x1 = float(input("ENTER THE X COORDINATES OF KNOWN POINT P1: "))
y1 = float(input("ENTER THE Y COORDINATES OF KNOWN POINT P1: "))
x2 = float(input("ENTER THE X COORDINATES OF KNOWN POINT P2: "))
y2 = float(input("ENTER THE Y COORDINATES OF KNOWN POINT P2: "))
dist1 = float(input("ENTER THE MEASURED HORIZONTAL DISTANCE IN METER UNIT FROM UNKNOWN POINTS A TO P1:"))
dist2 = float(input("ENTER THE MEASURED HORIZONTAL DISTANCE IN METER UNIT FROM UNKNOWN POINTS A TO P2:"))
beta = float(input("ENTER THE MEASURED HORIZONTAL ANGLE IN GRAD UNIT AT UNKNOWN POINTS A:"))

# CALCULATE THE AZIMUTH VALUE FROM KNOWN POINT P1 TO KNOWN POINT P2

# azimuth: açıklık açısı
if x1 == x2 and y1 > y2:
    azimuth = 300
elif x1 == x2 and y1 < y2:
    azimuth = 100
elif y1 == y2 and x1 > x2:
    azimuth = 200
elif y1 == y2 and x1 < x2:
    azimuth = 0
else:
    azimuth = (math.atan(abs(y2 - y1) / abs(x2 - x1)) * 200 / math.pi)
# 1. Quadrant
if (y2 - y1) > 0 and (x2 - x1) > 0:
    azimuth = azimuth
# 2. Quadrant
elif (y2 - y1) > 0 and (x2 - x1) < 0:
    azimuth = 200 - azimuth
# 3.Quadrant
elif (y2 - y1) < 0 and (x2 - x1) < 0:
    azimuth = 200 + azimuth
# 4.Quadrant
elif (y2 - y1) < 0 and (x2 - x1) > 0:
    azimuth = 400 - azimuth

print("Azimuth from P1 to P2:", format(azimuth, '.4f'), "grad")

# dist 3 is the horizontal distance from P1 to P2.

dist3 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Horizontal distance from P1 to P2:", format(dist3, '.2f'), "meter")

# CALCULATE THE INTERIOR ANGLES AT P1 AND P2
# USE THE SINUS THEOREM FOR P1 P2 A
# alfa for P2 and teta for P1

alfa = math.asin((dist1 * math.sin(beta * (math.pi / 200))) / dist3)

# convert alfa to grad unıt
alfa = alfa * (200 / math.pi)
print("alfa:", format(alfa, '.4f'), "grad")
teta = math.asin((dist2 * math.sin(beta * (math.pi / 200))) / dist3)
# convert to teta in grad unit
teta = teta * (200 / math.pi)
print("teta:", format(teta, '.4f'), "grad")

# check the total interior angle


total_angle = beta + teta + alfa

total_angle = float(format(total_angle, ".4f"))

if total_angle == 200:
    print(" Total İnterior Angle is 200 grad", "OK")
else:
    print("Check the Angles")

# CALCULATE THE AZIMUTH FROM P1 TO A

azimuth2 = azimuth + teta

if azimuth2 > 400:
    azimuth2 = azimuth2 - 400

print("Azimuth from P1 to A:", format(azimuth2, '.4f'), "grad")

# CALCULATE THE COORDINATES OF POINT A

xA1 = x1 + dist1 * math.cos(azimuth2 * math.pi / 200)
yA1 = y1 + dist1 * math.sin(azimuth2 * math.pi / 200)

print("Coordinates of A:", "X:", format(xA1, '.2f'), "meter", "Y:", format(yA1, '.2f'), "meter")

# Control of coordinates of point A
# Calculate the corrdinate of point A from starting point P2
# At first calculate the azimuth from P2 to P1

if azimuth < 200:
    azimuth3 = azimuth + 200
elif azimuth > 200:
    azimuth3 = azimuth - 200

print("Azimuth from P2 to P1:", format(azimuth3, '.4f'), "grad")

# CALCULATE THE AZIMUTH FROM P2 TO A

azimuth4 = azimuth3 - alfa

if azimuth4 > 400:
    azimuth4 = azimuth3 - 400

print("Azimuth from P2 to A:", format(azimuth4, '.4f'), "grad")

# CALCULATE THE COORDINATES OF POINT A

xA2 = x2 + dist2 * math.cos(azimuth4 * math.pi / 200)
yA2 = y2 + dist2 * math.sin(azimuth4 * math.pi / 200)

print("Control of Coordinates of Point A")

print("Coordinates of A:", "X:", format(xA2, '.2f'), "Y:", format(yA2, '.2f'), "meter")

"""
sample input:

x1:1000
y1:1000
x2:1008
y2:1006
dist1:6
dist2:8
beta:100 grad

"""