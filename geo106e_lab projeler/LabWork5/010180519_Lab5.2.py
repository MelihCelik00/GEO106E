import math

def slope_519(xa_519, xb_519, ya_519, yb_519, za_519, zb_519):
    
    dist_519 = math.sqrt((xb_519-xa_519)**2+(yb_519-ya_519)**2+(zb_519-za_519)**2)
    
    print("Distance = ",format(dist_519,".2f"))

    return

slope_519(1257.23, 1861.47, 1526.48, 1755.20, 120.0, 88.0)