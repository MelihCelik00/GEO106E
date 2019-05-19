for a_519 in range(0,10):
    for c_519 in range(0,10):
        for b_519 in range(1,10):
            if (11*(a_519+b_519+c_519) == 100*b_519 + 10*c_519 + a_519):
                print("A, B, C: {}, {}, {}".format(a_519,b_519,c_519))