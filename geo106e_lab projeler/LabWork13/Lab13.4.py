# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

# Import coordinates of Continent borders
pid, y, x = np.loadtxt("traverse.txt",
					delimiter=" ",
					skiprows= 1,
					unpack=True,
					dtype= [('PID','U10'),('Y',float),('X',float)])

# Create a figure
plt.figure("Traverse Sketch")
plt.title("Traverse Sketch") # figure title
plt.xlabel("Y (m)") # Label of x axis
plt.ylabel("X (m)") # Label of y axis

axes = plt.gca()
axes.set_xlim([4559000,4559400])
axes.set_ylim([368000,369500])

plt.scatter(x[0],y[0], marker="^", c="black", s = 24)
plt.annotate(pid[0], (x[0],y[0]), fontsize=16)
plt.scatter(x[1],y[1], marker="^", c="black", s = 24)
plt.annotate(pid[1], (x[1],y[1]), fontsize=16)
plt.scatter(x[2],y[2], marker="o", c="black", s = 24)
plt.annotate(pid[2], (x[2],y[2]), fontsize=16)
plt.scatter(x[3],y[3], marker="o", c="black", s = 24)
plt.annotate(pid[3], (x[3],y[3]), fontsize=16)
plt.scatter(x[4],y[4], marker="o", c="black", s = 24)
plt.annotate(pid[4], (x[4],y[4]), fontsize=16)
plt.scatter(x[5],y[5], marker="^", c="black", s = 24)
plt.annotate(pid[5], (x[5],y[5]), fontsize=16)
plt.scatter(x[6],y[6], marker="^", c="black", s = 24)
plt.annotate(pid[6], (x[6],y[6]), fontsize=16)

plt.plot(x,y, c="black", linewidth=.5)
