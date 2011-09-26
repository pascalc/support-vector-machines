#!/usr/bin/env python
import random
import pprint
from cvxopt import matrix

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