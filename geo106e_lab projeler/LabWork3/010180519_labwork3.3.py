import math
# My name is Melih Safa Çelik and my student id is 010180519
angle_519 = float(input("Enter a angle in degree:"))

radius_519 = angle_519*(math.pi / 180)
sin_519 = math.sin(radius_519)
cos_519 = math.cos(radius_519)
tan_519 = math.tan(radius_519)

print("Sine of the angle",angle_519 , "is",format(sin_519,".2f") )
print("Cosine of the angle", angle_519 ,"is", format(cos_519,".2f"))
print("Tangent of the angle", angle_519 ,"is", format(tan_519,".2f"))