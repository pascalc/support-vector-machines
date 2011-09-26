#!/usr/bin/env python
from cvxopt.base import matrix
from cvxopt.solvers import qp

import random, math, numpy, pprint, matplotlib

TRESHOLD = math.pow(10, -5)

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
	q = numpy.array([1 for x in range(N)])
	h = numpy.array([0 for x in range(N)])
	G = -identity(N)

	r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	alpha = list(r['x'])
	return alpha

def indicator_function(new_dp, alpha):
	"INPUT the data point to be classified and non-zero alpha values with corresponding data point"
	"RETURN true iff correctly classified"
	def evaluate(a, i, x_, x):
		return a*i*linear_kernel(x_, x)
	value = 0;
	for (a, dp) in alpha:
		value += evaluate(a, dp[2], new_dp, dp)
	
	return value

def linear_kernel(x,y):
	res = matrix(x).trans() * matrix(y) + 1
	return res[0]

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
P = buildP(data)

# Solve the quadractic problem
alpha = solve_qp(P)

# Map the alpha values to their corresponding data points
#data_alpha = zip(alpha, data) 

# Sort out the positive using TRESHOLD
#positive_alpha = [(x, a) for (x, a) in data_alpha if a > TRESHOLD]

# Classify a new data point using the indicator function
# indicators(new_dp, positive_alpha)

#print data
#pp = pprint.PrettyPrinter(depth=2)
#pp.pprint(map(repr,buildP(data)))