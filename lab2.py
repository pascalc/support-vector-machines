#!/usr/bin/env python
from cvxopt.base import matrix
from cvxopt.solvers import qp

import math, numpy
import data

THRESHOLD = math.pow(10, -5)
DEBUG = 1

def solveQP(P):
	"INPUT is a matrix P with dim NxN"
	"RETURN alpha that max/min? shiiiiit"
	def identity(n):
		"INPUT integer n"
		"RETURN identity matrix of size n"
		I = matrix(0.0, (n, n))
		I[::n+1] = 1.0
		return I
	
	N = len(P)
	q = numpy.ones((N,1))*(-1)
	h = numpy.zeros((N,1))
	numpy.transpose(h)
	G = (-1)*identity(N)
	
	r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
	alpha = list(r['x'])
	return alpha

def indicatorFunction(new_dp, alpha_list, kernel_function):
	"INPUT the data point to be classified and non-zero alpha values with corresponding data point"
	"RETURN indicator value, positive if correctly classified"
	value = 0;
	for (a, dp) in alpha_list:
		indicator = dp[2]
		point = (dp[0], dp[1])
		value += a*indicator*kernel_function(new_dp,point)
	
	return value

def linearKernel(x,y):
	res = matrix(x).trans() * matrix(y) + 1
	return res[0]

def radialBasisKernel(x, y):
	#Deterine a good value for sigma
	#http://en.wikipedia.org/wiki/Support_vector_machine#Properties
	#http://en.wikipedia.org/wiki/Cross-validation_%28statistics%29
	sigma = math.pow(2, 6)
	def sub_vector(x, y):
		z = matrix(x) - matrix(y)
		return z[0]
	
	enumerator = math.pow(sub_vector(x, y), 2)
	denominator = 2*math.pow(sigma, 2)
	K = math.exp((-1)*(enumerator / denominator))

	return K

def buildP(raw_data, kernel_function):
	"INPUT data, kernel function K"
	"RETURN matrix P(i,j) = t(i)*t(j)*K(x(i), x(j))"
	P = []
	data = map(lambda r: (r[0],r[1]), raw_data)
	indicators = map(lambda r: r[2], raw_data)
	for i in range(len(data)):
		x = data[i]
		row = []
		for j in range(len(data)):
			y = data[j]
			row += [indicators[i]*indicators[j]*kernel_function(x,y)]
		P += [row]
	return P

def debug(message):
	if DEBUG == 0:
		return
	print message

def main(test):
	data = test.getData()
	classify = test.classify

	kernel = linearKernel
	kernel = radialBasisKernel

	P = buildP(data, kernel)

	# Solve the quadractic problem
	alpha = solveQP(P)
	debug("\nalpha = " + str(alpha))

	# Map the alpha values to their corresponding data points
	data_alpha = zip(alpha, data) 
	debug("\nAlpha values with corresponding points\n" + str(data_alpha))

	# Sort out the positive using THRESHOLD
	positive_alpha = filter(lambda x: x[0] >= THRESHOLD, data_alpha)
	debug("\nPositive alpha\n" + str(positive_alpha))


	# Classify a new data point using the indicator function
	classify_list = []
	for p in classify:
		classify_list += [(indicatorFunction(p, positive_alpha, kernel), p[0], p[1])]

	correct_classified = filter(lambda x: x[0] > 0, classify_list)
	debug("\nCorrect classified examples: " + str(correct_classified))
	
	incorrect_classified = filter(lambda x: x[0] <= 0, classify_list)
	debug("\nIncorrect classified examples: " + str(incorrect_classified))

	test.plotData()
	test.plotPositiveAlpha(positive_alpha)
	#test.plotDecisionBoundary(indicatorFunction, kernel)
