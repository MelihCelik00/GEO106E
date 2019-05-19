import math
class ellipsoid:
    def __init__(self, a_519, b_519):
        self.a_519 = a_519
        self.b_519 = b_519
    def flattening(self):
        f = (self.a_519-self.b_519)/self.a_519 # 1/f
        return f

    def eccentricity(self):
        e1_519 = math.sqrt(1- (b_519**2/a_519**2))
        e2_519 = math.sqrt((a_519**2/b_519**2) - 1)
        return e1_519, e2_519

a_519 = 6378137.0 #semi-major axis in meters
b_519 = 6356752.3141 # semi-major axis in meters

myEllipsoid = ellipsoid(a_519,b_519)
flatening = myEllipsoid.flattening()
print("Flattening of the ellipsoid is", format(flatening,".8f"))
e1_519,e2_519 = myEllipsoid.eccentricity()
print("First and seccond eccentricity of the ellipsoid is",format(e1_519,".8f"), "and", format(e2_519,".8f"))