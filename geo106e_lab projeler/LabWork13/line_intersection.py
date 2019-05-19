import numpy as np

def line_from_points(p1, p2):
	if p1 == p2:
		raise ValueError("Points are Not Distinct...")
	else:
		x1, y1 = p1[0], p1[1]
		x2, y2 = p2[0], p2[1]
	# line for two points
	# ((y - y1) / (x - x1)) = ((y2-y1)/(x2-x1))
	# check if line is vertical x2 == x1
	if x2 == x1:
		# ax + by + c = 0
		# ax + by = -c
		# line is vertical -> x = -c
		a, b, c = 1, 0, -x1
	else:
		m = ((y2-y1)/(x2-x1))
		a, b, c = (-m), 1, (m*x1-y1)
	return a, b, c

def line_intersection(line1, line2):
	a1, b1, c1 = line_from_points(line1[0], line1[1])
	a2, b2, c2 = line_from_points(line2[0], line2[1])
	a = np.array([[a1, b1], [a2, b2]])
	b = np.array([-c1, -c2])
	x, y = np.linalg.solve(a, b)
	return x, y 

line1 = ((0.5, 0.5), (1.5, 0.5))
line2 = ((1, 0), (1, 2))

intersection = line_intersection(line1, line2)
print(intersection)



