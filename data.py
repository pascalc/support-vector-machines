#!/usr/bin/env python

import random



points1 = [ (random.normalvariate(1, 0.5),
				random.normalvariate(1.5, 0.5), 
				1.0)
			for i in range(50) ]

points2 = [ (random.normalvariate(2, 1.5),
				random.normalvariate(0.5, 2),
				-1.0)
			for i in range(50) ]