# -*- coding: utf-8 -*-
# Project Euler 35

from PEtools import *

Primes = set(Sieve(10**6))

def Rotations(n):
	# returns the set the rotations of the integer n
	string = str(n)
	rotations = set()
	for j in range(len(string)):
		rotation = int(string[j:len(string)] + string[:j])
		rotations = rotations.union({rotation})
	return rotations

CircularPrimes = []

for p in Primes:
	if len(Rotations(p).intersection(Primes)) == len(Rotations(p)):
		CircularPrimes.append(p)

print(len(CircularPrimes)) # 55
