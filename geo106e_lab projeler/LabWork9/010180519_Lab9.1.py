def BabylonAlgo_519(num_519):

    init_guess_519 = abs(float(num_519 / 2))
    e_519 = 0.00001
    while True:
        newg_519 =  ((init_guess_519 + (num_519/init_guess_519))/2)
        if (abs(newg_519 - init_guess_519) <= e_519):
            return newg_519
        else:
            init_guess_519 = newg_519