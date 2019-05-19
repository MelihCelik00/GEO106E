def tribonacci_519(n_519):
    triboList_519 = []
    a_519,b_519,c_519= 0,1,1
    triboList_519.append(a_519)
    for i_519 in range(n_519-1):
        a_519,b_519,c_519 = b_519,c_519,a_519+b_519+c_519
        triboList_519.append(a_519)
    return triboList_519

inp_519 = int(input("Enter the number of terms in Tribonacci series: "))

print(tribonacci_519(inp_519))