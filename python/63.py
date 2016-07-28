# -*- coding: utf-8 -*-
# Project Euler 50

from math import ceil

designerNumbers = []

for n in range(1,23):
	for k in range(ceil(10**((n-1)/n)), 10):
		designerNumbers.append(k**n)

print(len(designerNumbers)) # 49
