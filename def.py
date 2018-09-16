def quadratic(a, b, c):
	if a==0:
		raise TypeError('a<>0')
	x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
	return x1, x2
