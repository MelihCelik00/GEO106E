def azimuth_519(tAB_519,BB_519):
    K_519 = tAB_519 + BB_519
    
    if(K_519<200):
        tBC1_519 = tAB_519 + BB_519 + 200
        print("tBC is: ",format(tBC1_519,".4f"))

    elif(200<=K_519<= 600):
        tBC2_519 = tAB_519 + BB_519 - 200
        print("tBC is: ",format(tBC2_519,".4f"))

    else:
        tBC3_519 = tAB_519 + BB_519 - 600
        print("tBC is: ",format(tBC3_519,".4f"))

azimuth_519(115.1420,165.3140)