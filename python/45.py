# -*- coding: utf-8 -*-
# Project Euler 45

def Triangular(N):
	return int(N * (N + 1) / 2)

def Pentagonal(N):
	return int(N * (3*N - 1) / 2)

def Hexagonal(N):
	return N * (2*N - 1)

N = 100000

TriangularNumbers = [Triangular(n) for n in range(N)]

PentagonalNumbers = [Pentagonal(n) for n in range(N)]

HexagonalNumbers = [Hexagonal(n) for n in range(N)]

AllNumbers = TriangularNumbers + PentagonalNumbers + HexagonalNumbers
AllNumbers.sort()

for j in range(3*N - 3):
	if AllNumbers[j] == AllNumbers[j+1] and AllNumbers[j+1] == AllNumbers[j+2]:
		print(AllNumbers[j])

# 1533776805

