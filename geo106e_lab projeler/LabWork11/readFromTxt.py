# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:02:32 2018

@author: geoms
"""

import numpy as np

matrix1 = np.genfromtxt("matrix1.txt", skip_header=3)
matrix2 = np.genfromtxt("matrix2.txt", skip_header=3)
carpim  = np.dot(matrix1, np.transpose(matrix2))

