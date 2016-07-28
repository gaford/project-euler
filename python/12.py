# -*- coding: utf-8 -*-
# Project Euler 12

from math import sqrt

def triangular(N):
	return int(N * (N+1) / 2)

# def triangularNumbers(N):
# 	return [triangular(j) for j in range(1,N+1)]

# numberOfDivisors = []

# for N in range(15000):
# 	t = triangular(N)
# 	divisors = []
# 	x = 1
# 	while x < sqrt(t) + 1:
# 		if t % x == 0:
# 			divisors.append(x)
# 			divisors.append(int(t/x))
# 			x += 1
# 		else:
# 			x += 1
# 	numberOfDivisors.append(len(divisors))

# for j in range(len(numberOfDivisors)):
# 	if numberOfDivisors[j] > 500:
# 		print(j)

# first triangular number with more than 500 divisors is triangular(12375)
print(triangular(12375))

