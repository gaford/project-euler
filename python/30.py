# -*- coding: utf-8 -*-
# Project Euler 30

def SumOfDigitsFifthPowers(n):
	string = str(n)
	output = 0
	for digit in string:
		output += int(digit)**5
	return output

totalSum = 0
for j in range(2,200000):
	if j == SumOfDigitsFifthPowers(j):
		print(j)
		totalSum += j

print(totalSum) # 443839
