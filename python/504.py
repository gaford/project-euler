# -*- coding: utf-8 -*-
# Project Euler 504

from math import sqrt
from fractions import gcd

def InteriorLatticePoints(a,b,c,d):
    # returns the number of strictly contained lattice points in the
    # quadrilateral (a,0)--(0,b)--(-c,0)--(0,-d)
    area = (a+c)*(b+d)/2
    boundaryPoints = gcd(d,c) + gcd(b,c) + gcd(d,a) + gcd(b,a)
    # apply Pick's Theorem
    return int(area + 1 - boundaryPoints/2)

Squares = [n**2 for n in range(160)]

slots = [0] * (160**2)

m = 100

# SLOW
for a in range(1,m+1):
	for b in range(1,m+1):
		for c in range(1,m+1):
			for d in range(1,m+1):
				# print((a,b,c,d),"has", InteriorLatticePoints(a,b,c,d), \
				# 	"interior lattice points")
				slots[InteriorLatticePoints(a,b,c,d)] += 1

# OUTPUT
with open("504-output.txt","w") as output:
	for entry in slots:
		output.write(str(entry) + "\n")

# COUNT
count = 0
for square in Squares:
	count += slots[square]
print(count) # 694687

# squareSlots = []
# for square in Squares:
# 	squareSlots.append(slots[square])
# squareSlots = list(filter(None,squareSlots))
# print(squareSlots)
