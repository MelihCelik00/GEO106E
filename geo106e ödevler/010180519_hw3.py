def fibonacci_519(n_519):
    fiboList_519 = []
    a_519,b_519= 0,1
    fiboList_519.append(a_519)
    for i_519 in range(n_519-1):
        a_519,b_519 = b_519,a_519+b_519
        fiboList_519.append(a_519)
    return fiboList_519