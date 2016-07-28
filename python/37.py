# -*- coding: utf-8 -*-
# Project Euler 43

from PEtools import Sieve

Primes = set(Sieve(1000000))
ValidPrimes = Primes - {2,3,5,7}
TruncateablePrimes = set()

def Truncate(n):
	# return the set of left and right truncations of n
	string = str(n)
	truncations = set()
	for j in range(0,len(string)):
		truncations = truncations.union({int(string[j:]),int(string[:j+1])})
	return truncations

for p in ValidPrimes:
	if len(Truncate(p) & Primes) == len(Truncate(p)):
		TruncateablePrimes = TruncateablePrimes.union({p})

print(len(TruncateablePrimes)) # 11
print(TruncateablePrimes)
# {3137, 37, 739397, 73, 53, 373, 23, 3797, 313, 317, 797}

print(sum(TruncateablePrimes)) # 748317