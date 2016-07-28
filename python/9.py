# -*- coding: utf-8 -*-
# Project Euler 9

from math import sqrt

for a in range(1,1000):
	for b in range(a,1000):
		if int(a + b + sqrt(a**2 + b**2) == 1000):
			print(a,b)
			print(a*b*sqrt(a**2 + b**2))

