#!/usr/bin/env python

# Test class to simply testing and plot charts
# Authors: Joakim Carselind and Pascal Chatterjee
# Version: 2011-09-29

from cvxopt.base import matrix

import random, pylab, numpy, matplotlib
import lab2 as svm

class TestClass:
	"INPUT data tripple containaing, in order: positive data, negative data, classification points"
	"RETURN #N/A"
	def __init__(self, data):
		self.positive = data[0]
		self.negative = data[1]
		self.classify = data[2]

	def getData(self):
		data = self.positive + self.negative
		random.shuffle(data)
		return data
	
	def plotData(self):
		"Plots the positive and negative data points"
		pylab.hold(True)
		pylab.plot([p[0] for p in self.positive],
			[p[1]for p in self.positive],
		'bo')
		pylab.plot([p[0] for p in self.negative],
			[p[1]for p in self.negative],
		'ro')
		#pylab.show()

	def plotPositiveAlpha(self, alpha):
		"Plots the points belonging to the support vectors"
		pylab.hold(True)
		pylab.plot([a[1][0] for a in alpha],
			[a[1][1] for a in alpha],
		'yo')
		pylab.show()
			
	def plotDecisionBoundary(self, indicator, kernel):
		x_range = numpy.arange(-4, 4, 0.05)
		y_range = numpy.arange(-4, 4, 0.05)
		grid = matrix([ [indicator(x, y, kernel)
			for y in y_range]
			for x in x_range])
		pylab.contour(x_range, y_range, grid,
			(-1.0, 0.0, 1.0),
			colors=('red',' black', 'blue'),
			leninewidths=(1,3,1))
		pylab.show()

# Test when all positive/negative are above/below x-axis
def test1_linear():
	print "\n\t***** test1_linear *****\n"
	def classify():
		"classification points"
		v1_size = 20
		# y-value is set to normal(10, 0) meaning ALL will be above test points using normal(4,2)
		pos = [ (random.normalvariate(9, 10), random.normalvariate(10, 0)) for x in range(v1_size)]
		# y-value is set to normal(-10, 0) meaning ALL will be below negative test points using normal(-4,2)
		neg = [ (random.normalvariate(-5, 4), random.normalvariate(-10, 0)) for x in range(t1_size)]
		return pos + neg

	t1_size = 2
	first_qudrant = [ (random.normalvariate(5, 4), random.normalvariate(4, 2), 1) for x in range(t1_size)]
	second_quadrant = [ (random.normalvariate(-5, 4), random.normalvariate(4, 2), 1) for x in range(t1_size)]
	positive = first_qudrant + second_quadrant

	third_qudrant = [ (random.normalvariate(5, 4), random.normalvariate(-4, 2), -1) for x in range(t1_size)]
	fourth_qudrant = [ (random.normalvariate(-5, 4), random.normalvariate(-4, 2), -1) for x in range(t1_size)]
	negative = third_qudrant + fourth_qudrant

	return (positive, negative, classify())

def test2_linear():
	print "\n\t***** test2_linear ***** \n"
	
	def classify():
		v_size = 50

		return [(5,1), (2, 2)]
	
	positive = [ ( random.normalvariate(1.5,1) ,
			  random.normalvariate(0.5,1),
			1.0)
		  for i in range(5) ] + \
		[ ( random.normalvariate(1.5,1),
			random.normalvariate(0.5,1),
		  1.0)
		for i in range(5)]

	negative = [ (random.normalvariate(0.0,0.5) ,
				random.normalvariate(0.5,0.5) ,
				-1.0)
			for i in range(10) ]

	return (positive, negative, classify())

data = test1_linear()
#svm.main(TestClass(data))

data = test2_linear()
svm.main(TestClass(data))