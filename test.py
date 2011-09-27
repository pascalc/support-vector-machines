#!/usr/bin/env python

import random, lab2

# Test when all positive/negative are above/below x-axis
t1_size = 10;
def test_above_below_x_axis():
	pos_pos_x = [ (random.normalvariate(5, 4), random.normalvariate(4, 2), 1) for x in range(t1_size)]
	pos_neg_x = [ (random.normalvariate(-5, 4), random.normalvariate(4, 2), 1) for x in range(t1_size)]
	above_x = pos_pos_x + pos_neg_x

	neg_pos_x = [ (random.normalvariate(5, 4), random.normalvariate(-4, 2), -1) for x in range(t1_size)]
	neg_neg_x = [ (random.normalvariate(-5, 4), random.normalvariate(-4, 2), -1) for x in range(t1_size)]
	below_x = neg_neg_x + neg_pos_x

	data = above_x + below_x
	random.shuffle(data)

v1_size = 20;
def verify_above_below_x_axis():
	# y-value is set to normal(10, 0) meaning ALL will be above test points using normal(4,2)
	pos = [ (random.normalvariate(9, 10), random.normalvariate(10, 0), 1) for x in range(v1_size)]
	# y-value is set to normal(-10, 0) meaning ALL will be below negative test points using normal(-4,2)
	neg = [ (random.normalvariate(-5, 4), random.normalvariate(-10, 0), -1) for x in range(t1_size)]