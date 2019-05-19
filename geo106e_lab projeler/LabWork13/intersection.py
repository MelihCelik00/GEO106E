import math

# Surveying Intersection Computations
# ----------------------------
# Coordinate axes are switched
# as convention in surveying applications in Turkey

def calc_dist(ya, xa, yb, xb):
	ya = float(ya)
	xa = float(xa)
	yb = float(yb)
	xb = float(xb)
	dist = math.sqrt((yb - ya)**2 + (xb -xa)**2)	
	return dist

def calc_azimuth(ya, xa, yb, xb):

	# Coordinate Difference between Points
	# Coordinate Difference between Points
	dy = float(yb) - float(ya)
	dx = float(xb) - float(xa)
	if (dx == 0):
		if (yb>ya):
			azimuth_grad = 100.000
			return azimuth_grad
		elif (yb<ya):
			azimuth_grad = 0.0000
			return azimuth_grad
	#Calculate azimuth in radians
	azimuth_radians = math.atan((abs(dy)/abs(dx)))
	# Azimuth quadrant check
	if (dy > 0 and dx > 0):
		# Convert azimuth to grads from radians
		azimuth_grad = azimuth_radians * (200 / math.pi)
		# Azimuth is in first quadrant
		return azimuth_grad
	elif (dy > 0 and dx < 0):
		azimuth_grad = 200 - (azimuth_radians * (200 / math.pi))
		# Azimuth is in second quadrant
		return azimuth_grad
	elif (dy < 0 and dx < 0):
		azimuth_grad = 200 + (azimuth_radians * (200 / math.pi))
		# Azimuth is in third quadrant
		return azimuth_grad
	elif (dy < 0 and dx > 0):
		azimuth_grad = 400 - (azimuth_radians * (200 / math.pi))
		# Azimuth is in fourth quadrant
		return azimuth_grad


def intersection(xa, ya, xb, yb, alpha, beta, p_position):
	# p_position

	# Find the internal angle omega on unknown point p
	gama = 200 - (alpha + beta)
	# Find the disrance between known points (The length of line segment AB)
	distAB = calc_dist(ya, xa, yb, xb)
	distAP = (distAB * math.sin((beta * (math.pi / 200 )))) / (math.sin(gama * (math.pi / 200)))
	distBP = (distAB * math.sin((alpha * (math.pi / 200 )))) / (math.sin(gama * (math.pi / 200)))

	if (p_position) == "left":
		if (ya > yb):
			t_ba = calc_azimuth(yb, xb, ya, xa)
			t_bp = t_ba - beta
			t_ab = calc_azimuth(ya, xa, yb, xb)
			t_ap = t_ab + alpha

		elif (ya < yb):
			t_ab = calc_azimuth(ya, xa, yb, xb)
			t_ap = t_ab - alpha
			t_ba = calc_azimuth(yb, xb, ya, xa)
			t_bp = t_ba + beta

	elif p_position == "right":

		if (ya > yb):
			t_ba = calc_azimuth(yb, xb, ya, xa)
			tb_p = t_ba + beta
			t_ab = calc_azimuth(ya, xa, yb, xb)
			t_ap = t_ab - alpha

		elif (ya < yb):
			t_ab = calc_azimuth(ya, xa, yb, xb)
			t_ap = t_ab + alpha
			t_ba = calc_azimuth(yb, xb, ya, xa)
			t_bp = t_ba - beta

	yp_a = ya + distAP * math.sin((t_ap * (math.pi / 200 )))
	xp_a = xa + distAP * math.cos((t_ap * (math.pi / 200 )))

	yp_b = yb + distBP * math.sin((t_bp * (math.pi / 200 )))
	xp_b = xb + distBP * math.cos((t_bp * (math.pi / 200 )))

	# Calculate unkown point positions
	yp = (yp_a + yp_b) / 2
	xp = (xp_a + xp_b) / 2

	return yp, xp
