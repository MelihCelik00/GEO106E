# -*- coding: utf-8 -*-
"""
This module is created for GPS code mesaurement computations
GEO106E - Fundamentals of Programming - Spring Term 2018
Author: MSI
"""
# -----------------------------------------------------------------------------
import numpy as np
# -----------------------------------------------------------------------------
def readRinex(rinexFile):
	""" This program reads rinex observation file and returns 
	to C1 code mesaurements and approximate position.
	Usage : AppPos, SVList, C1 = readRinex("ista0010.18o")
	AppPos: Approximate position of receiver
	SVList: List of Visible Satellite Vehicles
	C1    : C1 code measurements
	""" 
	f = open(rinexFile) # open file
	rinexLines = f.readlines() # read lines in rinex file
	# -----------------------------------------------------------------------------
	# Read header lines
	line = 0 # initial line index
	while True:
		if 'APPROX POSITION XYZ' in rinexLines[line]:
			AppPos = rinexLines[line].split() # Split appro position line
			AppPos = AppPos[0:3] # Remove the text "APPROX POSITION XYZ" from the list
			AppPos = [float(i) for i in AppPos] # Convert string to float
			line +=1 # next line
		elif 'END OF HEADER' in rinexLines[line]:
			line +=1 # next line
			break # we reached to the end of header lines!
		else:
			line +=1 # next line
	del rinexLines[0:line] # Delete all the header lines
	# -----------------------------------------------------------------------------
	# Epoch(time) of observation
	epochLine = rinexLines[0].split() # split epoch line
	SV = epochLine[7][2:] 
	SVList = [SV[i:i+3] for i in range(0,len(SV),3)]
	del rinexLines[0] # Delete epoch line
	# -----------------------------------------------------------------------------
	# Take all C1 observations in a list
	C1 = [] # define an empty C1 list
	for line in rinexLines:
		observation = line.split() # split line of observation
		C1.append(float(observation[0])) # while appending to list, convert string to float
	C1 = np.array(C1) # convert C1 list to numpy array
	# -----------------------------------------------------------------------------
	return AppPos, SVList, C1 # function outputs
# -----------------------------------------------------------------------------
# Orbit File
def readOrbit(orbitFile):
	""" This program reads orbit file and returns to the coordinates of positioning satellites  (ephemeris)
	File format:
		1st column - Satellite Vehicle ID (SV)
		2nd column - X coordinates of SVs (X)
		3rd column - Y coordinates of SVs (Y)
		4th column - Z coordinates of SVs (Z)
		5th column - Satellite clock bias (dT)
	Usage: 
		orbit = readOrbit('igs19821.sp3')
	"""
	orbit = np.genfromtxt(orbitFile, # name of orbitFile
						skip_header=5, # skip first 5 lines
						names =['SV','X','Y','Z','dT'], # name of columns
						dtype=['U10', 'float64', 'float64', 'float64', 'float64']) # type of columns
	# Convert km to m unit
	orbit['X'] *= 1000
	orbit['Y'] *= 1000
	orbit['Z'] *= 1000
	orbit['dT'] *= 1e-6
	return orbit # function output
# -----------------------------------------------------------------------------
def pseudorange(rinexFile, orbitFile):
	""" This program solves pseudorange equations to find
	the position of a receiver using code measurements.
	Usage: 
		finalPosition = pseudorange(rinexFile, orbitFile)
	Output:
		X xoordinate of receiver ---> finalPosition[0]
		Y xoordinate of receiver ---> finalPosition[1]
		Z xoordinate of receiver ---> finalPosition[2]
		Satellite clock error of receiver ---> finalPosition[3]
	"""
	AppPos, SVList, C1 = readRinex(rinexFile)
	orbit = readOrbit(orbitFile)
	# ----------------------------
	for SV in orbit['SV']:
		if SV not in SVList:
			SVIndex = np.where(orbit['SV']==SV)
			orbit = np.delete(orbit, SVIndex)
	# -----------------------------------------------------------------------------
	c = 299792458.0 # speed of light
	distance = np.sqrt((orbit['X'] - AppPos[0])**2 + (orbit['Y'] - AppPos[1])**2 + (orbit['Z'] - AppPos[2])**2 )
	# -----------------------------------------------------------------------------
	# Solution of resection based on adjustment computation
	coeffMatrix = np.zeros([len(C1),4]) # len(C1): number of equations | 4 unknowns --> size: [len(C1),4]
	coeffMatrix[:,0] = ( AppPos[0] - orbit['X']) / distance
	coeffMatrix[:,1] = ( AppPos[1] - orbit['Y']) / distance
	coeffMatrix[:,2] = ( AppPos[2] - orbit['Z']) / distance
	coeffMatrix[:,3] = c 
	# -----------------------------------------------------------------------------
	# L matrix
	LMatrix = np.zeros([len(C1),1])
	LMatrix = C1 - distance + c * orbit['dT']
	# -----------------------------------------------------------------------------
	# Adjustment Computation
	NMatrix = np.linalg.inv(np.dot(np.transpose(coeffMatrix), coeffMatrix)) # inverse of N
	nMatrix = np.matmul(np.transpose(coeffMatrix), LMatrix)
	XMatrix = np.dot(NMatrix, nMatrix) # Matrix of Unknowns
	# -----------------------------------------------------------------------------
	posFinal = [ AppPos[0] + XMatrix[0], AppPos[1] + XMatrix[1], AppPos[2] + XMatrix[2], XMatrix[3]]
	return posFinal # function output

# END OF FILE
#------------------------------------------------------------------------------
pos = pseudorange("ista0010.18o","igs19821.sp3")