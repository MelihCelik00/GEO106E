import math
class Point():
    def calculate_distance(ya_519,yb_519,xa_519,xb_519):
        deltay_519 = abs(yb_519-ya_519)
        deltax_519 = abs(xb_519-xa_519)

        dist_519 = math.sqrt((deltax_519**2) + (deltay_519**2))
        print("Distance(meters):",format(dist_519,".2f"))

Point.calculate_distance(1320.03,1234.76,1005.65,1000.34)