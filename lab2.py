#!/usr/bin/env python
from cvxopt.base import matrix
from cvxopt.solvers import qp

import random, math, numpy, pprint, matplotlib, test

TRESHOLD = math.pow(10, -9)

def generate_data():
	classA = [ ( random.normalvariate(1.5,1) ,
				  random.normalvariate(0.5,1),
				1.0)
			  for i in range(5) ] + \
			[ ( random.normalvariate(1.5,1),
				random.normalvariate(0.5,1),
			  1.0)
			for i in range(5)]

	classB = [ (random.normalvariate(0.0,0.5) ,
				random.normalvariate(0.5,0.5) ,
				-1.0)
			for i in range(10) ]
	data = classA + classB
	random.shuffle(data)
	return data

def solve_qp(P):
	"INPUT is a matrix P with dim NxN"
	"RETURN alpha that max/min? shiiiiit"
	def identity(n):
		"INPUT integer n"
		"RETURN identity matrix of size n"
		I = matrix(0.0, (n, n))
		I[::n+1] = 1.0
		return I
	
	N = len(P)
	q = numpy.ones( ( N, 1 ) )
	h = numpy.zeros( ( N, 1 ) )
	#q = numpy.ones((N, 1))*-1
	#h = numpy.zeros((N, 1))
	numpy.transpose(h)
	G = -identity(N)
	print "N = ", len(P)
	print "matrix(q).size = ", matrix(q).size
	print "matrix(h).size = ", matrix(h).size
	print "matrix(G).size = ", matrix(G).size
	print "matrix(P).size = ", matrix(P).size

	print matrix(q)
	print matrix(h)
	print matrix(G)
	print matrix(P)

	r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	alpha = list(r['x'])
	return alpha

def indicator_function(new_dp, alpha_list):
	"INPUT the data point to be classified and non-zero alpha values with corresponding data point"
	"RETURN true iff correctly classified"
	def evaluate(a, i, x_, x):
		return a*i*linear_kernel(x_, x)
	value = 0;
	for (a, dp) in alpha_list:
		indicator = dp[2]
		point = (dp[0], dp[1])
		value += evaluate(a, indicator, new_dp, point)
	
	return value

def linear_kernel(x,y):
	res = matrix(x).trans() * matrix(y) + 1
	return res[0]

def radial_basis_kernel(x, y, sigma):
	def sub_vector(x, y):
		#z = ((x[0] - y[0]), (x[1] - y[1])
		z = matrix(x) - matrix(y)

		return z[0]
	
	enumerator = math.pow(sub_vector(x, y))
	denumerator = math.pow(sigma, 2)
	K = math.exp(enumerator / denumerator)

	return K

def buildP(raw_data):
	P = []
	data = map(lambda r: (r[0],r[1]), raw_data)
	indicators = map(lambda r: r[2], raw_data)
	for i in range(len(data)):
		x = data[i]
		row = []
		for j in range(len(data)):
			y = data[j]
			row += [indicators[i]*indicators[j]*linear_kernel(x,y)]
		P += [row]
	return P
	
def printMatrix(matrix):
	for i in range(len(data)):
		for j in range(len(data)):
			print matrix[i][j]
		print

# Generate the test data
data = generate_data()

# Build the matrix P according to P(i,j) = t(i)*t(j)*K(x(i), x(j)) where K is kernel function
test_data = test.test1()
P = buildP(test_data)

# Solve the quadractic problem
alpha = solve_qp(P)

print "alpha = ", alpha

# Map the alpha values to their corresponding data points
#points = [(x, y) for (x,y,z) in data]
data_alpha = zip(alpha, data) 
print data_alpha

# Sort out the positive using TRESHOLD
positive_alpha = filter(lambda x: x[0] >= TRESHOLD, data_alpha)
print "TRESHOLD = ", TRESHOLD
print "Positive alpha\n", str(positive_alpha)

new_dp = (random.normalvariate(1, 0.5),  random.normalvariate(2, 0.25))
verification = test.verify1()
# Classify a new data point using the indicator function
value = indicator_function(new_dp, positive_alpha)

pos_list = []
for p in verification[0]:
	pos_list += [(indicator_function(p, positive_alpha), p[0], p[1])]
#pos_list = map(lambda x: indicator_function(x, positive_alpha), verification[0])
#neg_list = map(lambda x: indicator_function(x, positive_alpha), verification[1])

cor = filter(lambda x: x[0] > 0, pos_list)
not_cor = filter(lambda x: x[0] <= 0, pos_list)
print "\nCorrect classified examples:\n", str(cor)

print "\nIn-correct classified examples:\n", str(not_cor)
#print data
#pp = pprint.PrettyPrinter(depth=2)
#pp.pprint(map(repr,buildP(data)))