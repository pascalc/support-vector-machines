#!/usr/bin/env python

import random

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

points1 = [ (random.normalvariate(1, 0.5),
				random.normalvariate(1.5, 0.5)
			)
			for i in range(50) ]

points2 = [ (random.normalvariate(2, 1.5),
				random.normalvariate(0.5, 2)
			)
			for i in range(50) ]

points3 = points1 + points2
random.shuffle(points3)