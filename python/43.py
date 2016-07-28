# -*- coding: utf-8 -*-
# Project Euler 43

Digits8To10 = [('00' + str(17 * x))[-3:] for x in range(1,59) \
	if len(set(('00' + str(17 * x))[-3:])) == 3]

steps = [7,6,5,4,3,2,1]
divisor = {7 : 13, 6 : 11, 5 : 7, 4 : 5, 3 : 3, 2 : 2, 1:1}

DesignerPandigitals = Digits8To10

for step in steps:
	tempDigits = []
	for string in DesignerPandigitals:
		for n in range(10):
			candidate = str(n) + string
			if int(candidate[:3]) % divisor[step] == 0 \
				and len(set(candidate)) == 11 - step:
				tempDigits.append(candidate)
	DesignerPandigitals = tempDigits

IntegerDesignerPandigitals = [int(x) for x in DesignerPandigitals]

print(IntegerDesignerPandigitals)
print(sum(IntegerDesignerPandigitals)) # 16695334890
