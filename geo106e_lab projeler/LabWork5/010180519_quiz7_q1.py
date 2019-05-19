import math
ya_519 = float(input("Enter Point A's X coordinate:"))
xa_519 = float(input("Enter Point A's Y coordinate:"))
ab_azimuth_519 = float(input("Enter the azimuth angle between point A and point B:"))

yb_519 = ya_519 + (distance_sab_519 * math.sin(ab_azimuth_519))
xb_519 = xa_519 + (distance_sab_519 * math.cos(ab_azimuth_519))


distance_sab_519 = float(input("Enter the distance between point A and B:"))

print("Point B's X coordinate:", format(xb_519,".3f"))
print("Point B's Y coordinate:", format(yb_519,".3f"))