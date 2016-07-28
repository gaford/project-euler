# -*- coding: utf-8 -*-
# Project Euler 41

from PEtools import *

Primes = Sieve(10**7)
PandigitalPrimes = []

for prime in Primes:
	digitList = str(prime)
	digitSet = set(digitList)
	if digitSet == set([str(j) for j in range(1,len(digitList)+1)]):
		PandigitalPrimes.append(prime)

print(PandigitalPrimes[-1]) # 7652413

