# -*- coding: utf-8 -*-
# Project Euler 28

diagonalEntries = [1]

for j in range(1,(1001-1)//2+1):
	diagonalEntries.append(diagonalEntries[-1] + 2*j)
	diagonalEntries.append(diagonalEntries[-1] + 2*j)
	diagonalEntries.append(diagonalEntries[-1] + 2*j)
	diagonalEntries.append(diagonalEntries[-1] + 2*j)

print(sum(diagonalEntries)) # 669171001

# This only works for odd x odd square grids.

