# -*- coding: utf-8 -*-
# Project Euler 44

N = 3 * 10**3

def P(n):
	# nth Pentagonal number
	return n*(3*n-1)//2

def PentagonalTest(x):
	# tests if x is pentagonal
	# returns the index of the number if true
	# returns False if false
	index = ((24*x+1)**0.5 + 1)/6
	if index.is_integer() == True:
		return True
	else:
		return False

for n in range(1,N):
	for k in range(1,N-n):
		if PentagonalTest(P(n+k) + P(n)):
			if PentagonalTest(P(n+k) - P(n)):
				print(P(n+k)-P(n))

# 5482660
