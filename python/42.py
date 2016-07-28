# -*- coding: utf-8 -*-
# Project Euler 42

import string

with open('42-words.txt','r') as inputFile:
	words = inputFile.readline().split('","')

TriangularNumbers = [n*(n+1)//2 for n in range(1,10000)]

TriangularWords = []

def WordValue(x):
	# returns the value of the word by summing the letter values
	# according to 'A' = 1, 'B' = 2, etc.
	value = 0
	for letter in x:
		value += 1 + string.ascii_uppercase.index(letter)
	return value

for word in words:
	if WordValue(word) in TriangularNumbers:
		TriangularWords.append(word)

print(len(TriangularWords)) # 162