# -*- coding: utf-8 -*-

import intersection

# First point
Xa_519 = 26242.67
Ya_519 = 11314.51
# Second Point
Xb_519 = 25318.11
Yb_519 = 12450.24
# Mesaurements
alpha_519 = 38.4325
beta_519  = 73.4894

Yp_519, Xp_519 = intersection.intersection(Xa_519, Ya_519, Xb_519, Yb_519, alpha_519, beta_519, 'left')
print("Yp:", format(Yp_519,".2f"), "m")
print("Xp:", format(Xp_519,".2f"), "m")


