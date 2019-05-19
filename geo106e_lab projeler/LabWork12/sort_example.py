import numpy as np

# First define headers for the table as list with tuples
# containing headers and their data types as below

headers = [('year', int), ('province', 'S10'), ('population', int), ('percentage', float)]

# Population data

population = [(2016, 'Istanbul', 14804116, 18.55), (2016, 'Ankara', 5346518, 6.70), (2016, 'Izmir', 4223545, 5.29), (2016, 'Bursa', 2901396, 3.64)]

# Create a structured array

population_array = np.array(population, dtype=headers)
print("Population data: ")
print(population_array)
# Sort using population and print
print("Population data sorted using population ")
print(np.sort(population_array, order='population'))

# Sort using population percentage and print
print("Population data sorted using population percentage ")
print(np.sort(population_array, order='percentage'))

# Sort using population province and print
print("Population data sorted using population percentage ")
print(np.sort(population_array, order='province'))
