# -*- coding: utf-8 -*-
# Project Euler 26

# this is SLOW!
# quicker to just check primes

from decimal import Decimal, getcontext

TestNumbers = [n for n in range(1000) if n % 2 != 0 if n % 3 != 0 if n % 5 != 0]

def ExpandFractionAsDecimal(p,q,N):
	# expand p/q as a decimal to N places
	getcontext().prec = N
	return Decimal(p) / Decimal(q)

recordLength = 1
recordNumber = 0

for n in TestNumbers:
	testInput = str(ExpandFractionAsDecimal(1,n,3*n))
	for j in range(1,n):
		for k in range(1,n):
			if testInput[j:j+k] == testInput[j+k:j+2*k] and k <= recordLength:
				break
				break
			if testInput[j:j+k] == testInput[j+k:j+2*k] and k > recordLength:
				recordLength = k
				recordNumber = n
				print(n)
				break
				break

print()
print(recordNumber) # 983
print(recordLength) # 982
