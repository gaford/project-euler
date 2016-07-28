# -*- coding: utf-8 -*-
# Project Euler 39

maxPerimeter = 1000

Perimeters = [set()] * maxPerimeter
PerimetersCount = [0] * maxPerimeter

def PythagoreanTriple(m,n,k):
	# generates a Pythagorean triple
	return {k*(m**2 - n**2), k*2*m*n, k*(m**2 + n**2)}

for m in range(1,1000):
	for n in range(1,m):
		triples = set()
		k = 1
		while sum(PythagoreanTriple(m,n,k)) <= maxPerimeter:
			Perimeters[sum(PythagoreanTriple(m,n,k))-1] = \
				Perimeters[sum(PythagoreanTriple(m,n,k))-1] | \
				PythagoreanTriple(m,n,k)
			k += 1

for j in range(maxPerimeter):
	PerimetersCount[j] = len(Perimeters[j])

maxTriples = max(PerimetersCount)
print(PerimetersCount.index(maxTriples) + 1) # 840


