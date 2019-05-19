# -*- coding: utf-8 -*-
import math


def calc_dist(ya, xa, yb, xb):
    ya = float(ya)
    xa = float(xa)
    yb = float(yb)
    xb = float(xb)
    dist = math.sqrt((yb - ya)**2 + (xb -xa)**2)    
    return dist

def calc_azimuth(ya, xa, yb, xb):

    # Coordinate Difference between Points
    # Coordinate Difference between Points

    dy = float(yb) - float(ya)
    dx = float(xb) - float(xa)

    #Calculate azimuth in radians
    azimuth_radians = math.atan((abs(dy)/abs(dx)))
    # Azimuth quadrant check
    if dy > 0 and dx > 0:
        # Convert azimuth to grads from radians
        azimuth_grad = azimuth_radians * (200 / math.pi)
        print("Azimuth is in first quadrant")
        return azimuth_grad
    elif dy > 0 and dx < 0:
        azimuth_grad = 200 - (azimuth_radians * (200 / math.pi))
        print("Azimuth is in second quadrant")
        return azimuth_grad
    elif dy < 0 and dx < 0:
        azimuth_grad = 200 + (azimuth_radians * (200 / math.pi))
        print("Azimuth is in third quadrant")
        return azimuth_grad
    elif dy < 0 and dx > 0:
        azimuth_grad = 400 - (azimuth_radians * (200 / math.pi))
        print("Azimuth is ni fourth quadrant")
        return azimuth_grad
    elif dy == 0:
        if xb<xa:
            azimuth_grad = 100
        if xb >xa:
            azimuth_grad = 300
        return azimuth_grad
    elif dx == 0:
        if yb < ya:
            azimuth_grad = 200
        if yb > ya:
            azimuth_grad = 400
        return azimuth_grad
        
    else:
        print("Error: Azimuth is not in first four quadrant")


# Call the function with parameters and assign to variables
dist  = calc_dist(4879.554, 5263.621, 5416.215, 4138.130)
az = calc_azimuth(4879.554, 5263.621, 5416.215, 4138.130)

# Print results
print("-----------------------------")
print("Azimuth(grads): ", format(az, ".4f"))
print("Distance(meters): ", format(dist, ".3f"))
