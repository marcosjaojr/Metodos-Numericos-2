from math import sqrt

def runge_kutta5(temp_s, a, b, n):

	somatorio = 0
	h = float(b-a)/n

	ai = a
	for i in range(0,n):
		bi = ai + h
		k1 = F(temp_s,ai)
		k2 = F(temp_s + (h/4.0)*k1, ai + (h/4.0))
		k3 = F(temp_s + (h/8.0)*k1 + (h/8.0)*k2, ai + (h/4.0))
		k4 = F(temp_s - 1*(h/2.0)*k2 + h*k3, ai + 2*(h/4.0))
		k5 = F(temp_s + 3*(h/16.0)*k1 + 9*(h/16.0)*k4, ai + 3*(h/4.0))
		k6 = F(temp_s - 3*(h/7.0)*k1 + 2*(h/7.0)*k2 + 12*(h/7.0)*k3 - 12*(h/7.0)*k4 + 8*(h/7.0)*k5, bi)

		somatorio += (1/90.0)*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)
		ai = bi

	integral = somatorio

	return temp_s + integral

def F(s, t):
	return t*sqrt(s)

def start_value():
	# X0,Y0
	return 0, 1

x0, s0 = start_value()
temp_x = x0
temp_s = s0
for x in [x * 1 for x in range(x0+1,x0+11)]:
	temp_s = runge_kutta5(temp_s, temp_x, x, 1)
	print(str(x)+": "+str(temp_s))
	temp_x = x
