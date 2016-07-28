# -*- coding: utf-8 -*-
# Project Euler 38

stringDigits = ['1','2','3','4','5','6','7','8','9']

def IntegerConcatenation(x,n):
	stringMultiples = [str(x * y) for y in range(1,n+1)]
	outputString = ''
	for item in stringMultiples:
		outputString += item
	return int(outputString)

pandigitalNumbers = []

for x in range(100,1000):
	n = IntegerConcatenation(x,3)
	if sorted(str(n)) == stringDigits:
		pandigitalNumbers.append(n)

for x in range(1000,15000):
	n = IntegerConcatenation(x,2)
	if sorted(str(n)) == stringDigits:
		pandigitalNumbers.append(n)

print(len(pandigitalNumbers))
print(max(pandigitalNumbers)) # 932718654

