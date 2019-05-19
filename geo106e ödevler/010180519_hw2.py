def triangle_area_519(x1_519,y1_519,x2_519,y2_519,x3_519,y3_519):
        
    side1_519 = ((x3_519 - x1_519)**2 + (y3_519 - y1_519)**2)**(1/2)
    side2_519 = ((x2_519 - x1_519)**2 + (y2_519 - y1_519)**2)**(1/2)
    side3_519 = ((x2_519 - x3_519)**2 + (y2_519 - y3_519)**2)**(1/2)
    
    s_519 = (side1_519 + side2_519 + side3_519)/2

    area_519 = (s_519*(s_519 - side1_519)*(s_519 - side2_519)*(s_519 - side3_519))**(1/2)

    print("Coordinates of 1st corner ("+str(x1_519)+","+str(y1_519)+")")
    print("Coordinates of 1st corner ("+str(x2_519)+","+str(y2_519)+")")
    print("Coordinates of 1st corner ("+str(x3_519)+","+str(y3_519)+")")

    print("Area:",area_519)
    return area_519

triangle_area_519(1.5,-3.4,4.6,5.0,9.5,-3.4)