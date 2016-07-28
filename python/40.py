# -*- coding: utf-8 -*-
# Project Euler 40

digitStrings = [str(n) for n in range(200000)]

Champernowne = ''
for string in digitStrings:
	Champernowne += string

product = 1
for j in range(0,7):
	product *= int(Champernowne[10**j])
	print("The %sth digit is %s." % (str(10**j),Champernowne[10**j]))

print("The product of these digits is %s." % str(product))

