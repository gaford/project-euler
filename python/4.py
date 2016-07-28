# -*- coding: utf-8 -*-
# Project Euler 4

# want to find largest product of two three digit numbers which is a palindrome

# palindrome detector
def isPalindrome(x):
	entry = str(x)
	if entry == entry[::-1]:
		return True
	else:
		return False

largePalindromes = []

for x in range(900,1000):
	for y in range(x,1000):
		if isPalindrome(x*y):
			largePalindromes.append((x,y,x*y))

largePalindromes.sort()

print(largePalindromes)
