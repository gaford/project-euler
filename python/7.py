# -*- coding: utf-8 -*-
# Project Euler 7

# find the 10001st prime

import math

primes = []

limit = int(2 * 10001 * math.log(10001)) # prime number theorem bound

def isPrime(x):
	for prime in primes:
		if x % prime == 0:
			return False
	else:
		return True

for x in range(2,limit):
	if isPrime(x):
		primes.append(x)
	elif len(primes) == 10001:
		break

print(primes[10000])

# the 10001st prime is 104743.
