# -*- coding: utf-8 -*-
# Project Euler 22

nameFile = open('22-names.txt','r')

names = nameFile.read().split('","')

names.sort()

alphabetScore = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8,
	'I':9, \
	'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, \
	'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

def nameScore(name):
	score = 0
	for char in name:
		score += alphabetScore[char]
	return score

totalScore = 0

for j in range(len(names)):
	totalScore += (j+1) * nameScore(names[j])

print(totalScore)

nameFile.close()