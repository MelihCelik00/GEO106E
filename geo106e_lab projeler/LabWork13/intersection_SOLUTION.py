# -*- coding: utf-8 -*-

import intersection

# First point
Xa = 26242.67
Ya = 11314.51
# Second Point
Xb = 25318.11
Yb = 12450.24
# Mesaurements
alpha = 38.4325
beta  = 73.4894

Yp, Xp = intersection.intersection(Xa, Ya, Xb, Yb, alpha, beta, 'left')
print("Yp:", format(Yp,".2f"), "m")
print("Xp:", format(Xp,".2f"), "m")


