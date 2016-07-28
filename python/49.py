# -*- coding: utf-8 -*-
# Project Euler 49

from eulertools import Sieve
import itertools

Primes = Sieve(10**4)
FourDigitPrimes = [p for p in Primes if p >= 1000]

digits = '0123456789'

FourDigitChoices = [list(x) for x in \
	list(itertools.combinations_with_replacement(digits,4))]
DigitCount = [0] * len(FourDigitChoices)

PrimeGroups = [[] for j in range(len(FourDigitChoices))]

for p in FourDigitPrimes:
	digits = sorted(str(p))
	DigitCount[FourDigitChoices.index(digits)] += 1
	PrimeGroups[FourDigitChoices.index(digits)].append(p)

LongPrimeGroups = [x for x in PrimeGroups if len(x) >= 3]

for group in LongPrimeGroups:
	BigDifferences = [(x,y,y - x) for y in group for x in group if y > x]
	# Differences = [x[2] for x in BigDifferences]
	# for	j in range(len(BigDifferences)):
	# 	if Differences.count(Differences[j]) >=2:
	# 		print(BigDifferences[j])
	GoodDifferences = [(a,b) for a in BigDifferences for b in BigDifferences \
		if a[1] == b[0] and a[2] == b[2]]
	if len(GoodDifferences) > 0:
		print(GoodDifferences)