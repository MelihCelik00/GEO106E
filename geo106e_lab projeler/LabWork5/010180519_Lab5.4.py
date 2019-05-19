def rmse(meas_519):
    squared_errors_519 = []
    mean_519 = sum(meas_519) / len(meas)

    v1_square_519 = (meas_519[0] - mean_519)**2
    v2_square_519 = (meas_519[1] - mean_519)**2
    v3_square_519 = (meas_519[2] - mean_519)**2
    v4_square_519 = (meas_519[3] - mean_519)**2
    v5_square_519 = (meas_519[4] - mean_519)**2

    squared_errors_519.extend(v1_square_519, v2_square_519, v3_square_519, v4_square_519, v5_square_519)

    rmse = (sum(squared_errors_519) /  (len(squared_errors_519) - 1))**(1/2)

    print("RMS Error: " format(rmse, ".2f"))

    meas_519 = [120.05, 119.97, 120.03, 119.98, 120.06]

    rmse(meas_519)