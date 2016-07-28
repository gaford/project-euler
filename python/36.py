# -*- coding: utf-8 -*-
# Project Euler 36

limit = 10**6

Base10Pallindromes = [n for n in range(limit) if str(n) == str(n)[::-1]]

DoubleBasePallindromes = [n for n in Base10Pallindromes \
	if str(bin(n))[2:] == str(bin(n))[2:][::-1]]

print(len(DoubleBasePallindromes))
print(sum(DoubleBasePallindromes))

