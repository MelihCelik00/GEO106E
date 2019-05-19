import numpy as np_519

headers_519 = [("year",int),("province",'S10'),("population",int),("percentage",float)]

population_519 = [(2016,'Istanbul',14804116,18.55),(2016,'Ankara',5346518,6.70),(2016,'Izmir',4223545,5.29),(2016,'Bursa',2901396,3.64)]

population_arr_519 = np_519.array(population_519, dtype = headers_519)
print("Population data: ")
print(population_arr_519)

print("Population data sorted using population ")
print(np_519.sort(population_arr_519, order="population"))