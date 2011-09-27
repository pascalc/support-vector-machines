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

points1 = [ (random.normalvariate(1, 0.5),
				random.normalvariate(1.5, 0.5), 
				1)
			for i in range(50) ]

points2 = [ (random.normalvariate(2, 1.5),
				random.normalvariate(0.5, 2),
				1.0)
			for i in range(50) ]

pos_pos_x = [ (random.normalvariate(5, 4), 
				random.normalvariate(4, 2), 
				1) 
			for x in range(10)]
pos_neg_x = [ (random.normalvariate(-5, 4),
				random.normalvariate(4, 2),
				1) 
			for x in range(10)]

above_x = pos_pos_x + pos_neg_x

neg_pos_x = [ (random.normalvariate(5, 4), 
				random.normalvariate(-4, 2),
				-1) 
			for x in range(10)]
neg_neg_x = [ (random.normalvariate(-5, 4),
				random.normalvariate(-4, 2),
				-1) 
			for x in range(10)]

below_x = neg_neg_x + neg_pos_x
