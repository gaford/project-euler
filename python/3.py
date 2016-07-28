# -*- coding: utf-8 -*-
# Project Euler 3

from math import sqrt

# finding the largest prime factor of this number
N = 600851475143

# determining the divisors and quotients
# divisors = []
# quotients = []
# M = 10000000
# for j in range(1,M):
# 	if N % j == 0:
# 		quotient = N / j
# 		divisors.append(j)
# 		quotients.append(quotient)

# computed divisors
computedDivisors = [1, 71, 839, 1471, 6857, 59569, 104441, 486847, 1234169, \
	5753023]

computedDivisorsDivisibleBy71 = [j for j in computedDivisors if j % 71 == 0]
print(computedDivisorsDivisibleBy71)

computedDivisorsDivisibleBy839 = [j for j in computedDivisors if j % 839 == 0]
print(computedDivisorsDivisibleBy839)

computedDivisorsDivisibleBy1471 = [j for j in computedDivisors if j % 1471 == 0]
print(computedDivisorsDivisibleBy1471)

computedDivisorsDivisibleBy6857 = [j for j in computedDivisors if j % 6857 == 0]
print(computedDivisorsDivisibleBy6857)

# the largest prime factor is 6857

