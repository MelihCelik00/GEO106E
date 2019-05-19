import numpy as np_519

def line_from_points_519(p1_519, p2_519):
	if p1_519 == p2_519:
		raise ValueError("Points are Not Distinct...")
	else:
		x1_519, y1_519 = p1_519[0], p1_519[1]
		x2_519, y2_519 = p2_519[0], p2_519[1]
	# line for two points
	# ((y - y1) / (x - x1)) = ((y2-y1)/(x2-x1))
	# check if line is vertical x2 == x1
	if x2_519 == x1_519:
		# ax + by + c = 0
		# ax + by = -c
		# line is vertical -> x = -c
		a_519, b_519, c_519 = 1, 0, -x1_519
	else:
		m_519 = ((y2_519-y1_519)/(x2_519-x1_519))
		a_519, b_519, c_519 = (-m_519), 1, (m_519*x1_519-y1_519)
	return a_519, b_519, c_519

def line_intersection_519(line1_519, line2_519):
	a1_519, b1_519, c1_519 = line_from_points_519(line1_519[0], line1_519[1])
	a2_519, b2_519, c2_519 = line_from_points_519(line2_519[0], line2_519[1])
	a_519 = np_519.array([[a1_519, b1_519], [a2_519, b2_519]])
	b_519 = np_519.array([-c1_519, -c2_519])
	x_519, y_519 = np_519.linalg.solve(a_519, b_519)
	return x_519, y_519

line1_519 = ((0.5, 0.5), (1.5, 0.5))
line2_519 = ((1, 0), (1, 2))

intersection_519 = line_intersection_519(line1_519, line2_519)
print(intersection_519)

