import math

def function(slope_dist_519, zenith_angle_519):


    zenith_radian_519 = zenith_angle_519 * (math.pi / 200)
    horizontal_dist_519 = (slope_dist_519) * math.sin(zenith_radian_519)

    print("Horizontal Distance (meters) : ", format(horizontal_dist_519,".3f"))
function(127.834, 98.421)