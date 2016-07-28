# -*- coding: utf-8 -*-
# Project Euler 27

from PEtools import *

Primes = Sieve(1000)

def QuadraticFormula(n,a,b):
	return n**2 + a * n + b

RecordNumber = 0
RecordParameters = (0,0)

for a in range(-999,1000):
	for b in Primes:
		n = 0
		while IsPrime1(QuadraticFormula(n,a,b)):
			n += 1
		if n >= RecordNumber:
			RecordNumber = n
			RecordParameters = (a,b)

print("The record number is %s." % str(RecordNumber)) # 71
print("The record parameters are %s." % str(RecordParameters)) # (-61,971)
print("The product of the parameters is %s." % str(RecordParameters[0] * \
	RecordParameters[1])) # -59231



