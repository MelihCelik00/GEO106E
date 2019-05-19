def gcd_519(a_519,b_519):

    while (b_519!= 0):
        r_519 = a_519 % b_519

        if (r_519 == 0):
            return b_519
        else:
            a_519, b_519 = b_519,r_519

