# -*- coding: utf-8 -*-
# Project Euler 23

def ProperDivisorSum(n):
	divisors = {1}
	for j in range(2,int(n**0.5 + 1)):
		if n % j == 0:
			divisors = divisors.union({j}).union({n//j})
	return sum(divisors)

limit = 28124

AbundantNumbers = []
for n in range(1,limit):
	if ProperDivisorSum(n) > n:
		AbundantNumbers.append(n)

AbundantNumbersFile = open("23-abundant.txt","w")
for number in AbundantNumbers:
	AbundantNumbersFile.write(str(number) + "\n")

SumsOfAbundantNumbers = {x + y for x in AbundantNumbers \
	for y in AbundantNumbers if y <= x}

MyNumbers = set(range(1,limit)) - SumsOfAbundantNumbers

print(sum(MyNumbers))

AbundantNumbersFile.close()
