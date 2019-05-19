def lcm_519(num1_519,num2_519):

    if (num1_519>num2_519):
        greater_519 = num1_519
        smaller_519 = num2_519
    else:
        greater_519 = num2_519
        smaller_519 = num1_519

    i_519 = 0
    while True:

        if (greater_519 % num1_519 == 0 and greater_519 % num2_519 == 0):
            lcm_519 = greater_519
            return lcm_519
        else:
            i_519 += 1
            greater_519 = smaller_519*i_519

