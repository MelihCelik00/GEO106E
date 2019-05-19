# -*- coding: utf-8 -*-
"""
Created on Tue May  8 20:39:14 2018

@author: geoms
"""
import random
import matplotlib.pyplot as plt
import numpy as np
# Import coordinates of Continent borders
x_europe, y_europe = np.loadtxt("europe.txt", delimiter=",", unpack=True)
x_asia, y_asia = np.loadtxt("asia.txt", delimiter=",", unpack=True)
x_africa, y_africa = np.loadtxt("africa.txt", delimiter=",", unpack=True)
x_americaN, y_americaN = np.loadtxt("north_america.txt", delimiter=",", unpack=True)
x_americaS, y_americaS = np.loadtxt("south_america.txt", delimiter=",", unpack=True)
x_americaS, y_americaS = np.loadtxt("south_america.txt", delimiter=",", unpack=True)
x_austria, y_austria = np.loadtxt("austria.txt", delimiter=",", unpack=True)
x_antarctica, y_antarctica = np.loadtxt("antarctica.txt", delimiter=",", unpack=True)
# Import coordinates of Airports
x,y,code = np.loadtxt("airports.txt",
                        delimiter=",",
                        unpack=True,
                        dtype=[('Lon', float), ('Lat', float), ('code', 'U10')])
# Create a figure
plt.figure("Map of Airports")
plt.title("Map of Airports") # figure title
plt.xlabel("Latitude") # Label of x axis
plt.ylabel("Longitude") # Label of y axis
# Plot continents
plt.plot(x_europe, y_europe, linestyle='-', color="red")
plt.plot(x_asia, y_asia, linestyle='-', color="red")
plt.plot(x_africa, y_africa, linestyle='-', color="red")
plt.plot(x_americaN, y_americaN, linestyle='-', color="red")
plt.plot(x_americaS, y_americaS, linestyle='-', color="red")
plt.plot(x_austria, y_austria, linestyle='-', color="red")
plt.plot(x_antarctica, y_antarctica, linestyle='-', color="red")
# Plot airports
numbers = [random.randint(0,len(code)) for i in range(100)] # 100 random numbers
for i in numbers: # limited to 100 for speed
    plt.scatter(x[i],y[i], s=12)
    plt.annotate(code[i], (x[i],y[i]), fontsize=10) # label of airport
