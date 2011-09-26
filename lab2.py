#!/usr/bin/env python
from cvxopt.base import matrix
from cvxopt.solver import qp

import random, math, numpy, pprint, matlibplot

def TRESHOLD = math.pow(10, -5)

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
	N = len(data_set)
	q = numpy.array([x for 1 in range(N)])
	h = numpy.array([x for 0 in range(N)])
	G = -identity(N)
	def identity(n):
		"INPUT integer n"
    	"RETURN identity matrix of size n"
	    I = matrix(0.0, (n, n))
	    I[::n+1] = 1.0
	    return I
	
	#r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	#alpha = list(r['x'])
	#return alpha

def indicator_function(new_dp):
	"INPUT the data point to be classified"
	"RETURN true iff correctly classified"
	def evaluate(a, dp, new_dp):
		"INPUT alpha value a, data point dp"
		"RETURN value"
		return a*

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

data = generate_data()
print data
pp = pprint.PrettyPrinter(depth=2)
pp.pprint(map(repr,buildP(data)))