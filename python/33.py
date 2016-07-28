# -*- coding: utf-8 -*-
# Project Euler 33

from fractions import Fraction

cancellableDigits = '123456789'
digits = '0123456789'

digitCancellingFractions = set()

for digit1 in digits:
	for digit2 in cancellableDigits:
		for cancellableDigit in cancellableDigits:
			numerator = int(digit1 + cancellableDigit)
			denomenator = int(cancellableDigit + digit2)
			if Fraction(numerator,denomenator) == Fraction(int(digit1), \
					int(digit2)) and \
					Fraction(numerator,denomenator) != Fraction(1,1):
				digitCancellingFractions = digitCancellingFractions | \
					{(int(numerator),int(denomenator))}

print(digitCancellingFractions)

print(Fraction(49,98) * Fraction(19,95) * Fraction(16,64) * Fraction(26,65))