# -*- coding: utf-8 -*-
# Project Euler 34

from math import factorial

def DigitFactorial(x):
	# returns the sum of the factorials of the digits of x
	numberString = str(x)
	output = 0
	for digit in numberString:
		output += factorial(int(digit))
	return output

corral = []

for n in range(3,10**6):
	if n in [k * 10**5 for k in range(10)]:
		print("At %s." % n)
	if DigitFactorial(n) == n:
		corral.append(n)

print(corral) # 1 and 2 do not count
print(sum(corral)) # 40730

