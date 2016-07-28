# -*- coding: utf-8 -*-
# Project Euler 21

def ProperDivisorSum(n):
	divisors = [1]
	for j in range(2,int(n**0.5 + 1)):
		if n % j == 0:
			divisors.append(j)
			divisors.append(n//j)
	return sum(divisors)

myList0 = []
for n in range(1,10000):
	myList0.append((n,ProperDivisorSum(n)))

myList1 = []
for n in range(1,10000):
	myList1.append((ProperDivisorSum(n),n))

myList2 = myList0 + myList1

myList2.sort(key = lambda x: x[0])

for j in range(len(myList2)-1):
	if myList2[j] == myList2[j+1]:
		print(myList2[j])

print(220 + 284 + 1184 + 1210 + 2620 + 2924 + 5020 + 5564 + 6232 + 6368)
# 31626