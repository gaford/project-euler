# -*- coding: utf-8 -*-
# Project Euler 18

from itertools import chain

# number of rows
N = 15

inputFile = open('18-input.txt','r')
rawData = list(inputFile)

for j in range(len(rawData)):
	rawData[j] = rawData[j].replace('\n','')

Triangle = {}
for j in range(len(rawData)):
	for k in range(0,len(rawData[j]),3):
		Triangle[(-j + 2*k//3,j)] = int(rawData[j][k:k+2])

# building the path motions
directions = ([-1] * 2**(N-2)) + ([1] * 2**(N-2))
positions = [0] * 2**(N-1)
pathTotals = [0] * 2**(N-1)


for j in range(N):
	for k in range(len(positions)):
		pathTotals[k] += Triangle[(positions[k],j)]
	directions = list(chain.from_iterable(zip(directions[0:2**(N-2)], \
		directions[2**(N-2):])))
	positions = [x + y for x,y in zip(positions,directions)]

print(max(pathTotals)) # 1074

