# -*- coding: utf-8 -*-
# Project Euler 32

from math import factorial
import itertools

digits = [1,2,3,4,5,6,7,8,9]
stringDigits = [str(x) for x in digits]

pandigitalProducts = set()

fiveDigits = list(itertools.permutations(stringDigits,5))

OneTimesFour = [(int(x[0]),int(x[1] + x[2] + x[3] + x[4])) \
	for x in fiveDigits]

for item in OneTimesFour:
	product = item[0] * item[1]
	string = str(item[0]) + str(item[1]) + str(product)
	if sorted(string) == stringDigits:
		pandigitalProducts = pandigitalProducts | {product}

TwoTimesThree = [(int(x[0] + x[1]), int(x[2] + x[3] + x[4])) \
	for x in fiveDigits]

for item in TwoTimesThree:
	product = item[0] * item[1]
	string = str(item[0]) + str(item[1]) + str(product)
	if sorted(string) == stringDigits:
		pandigitalProducts = pandigitalProducts | {product}

print(pandigitalProducts)
print(sum(pandigitalProducts)) # 45228


