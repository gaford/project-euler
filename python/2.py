# -*- coding: utf-8 -*-
# Project Euler 2

from math import sqrt

# Fibonnaci number generator
def Fibonnaci(N):
	goldenRatio = (1 + sqrt(5))/2
	goldenRatio2 = (1 - sqrt(5))/2
	output = 1 / sqrt(5) * (goldenRatio**N - goldenRatio2**N)
	return int(output)

# empty sequence
sequence = []

# filling the sequence with the empty Fibonnacis
for j in range(100):
	if (Fibonnaci(j) <= 4000000) and (Fibonnaci(j) % 2 == 0):
		sequence.append(Fibonnaci(j))

print(sequence)

print(sum(sequence))

