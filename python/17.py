# -*- coding: utf-8 -*-
# Project Euler 17

def Englishify(x):
	string = str(x)
	string = '0' * (4 - len(string)) + string
	ones = int(string[-1])
	tens = int(string[-2])
	hundreds = int(string[-3])
	thousands = int(string[-4])

	onesStrings = ['','one','two','three','four','five','six','seven', \
		'eight','nine']
	tensStrings = ['','','twenty','thirty','forty','fifty','sixty','seventy', \
		'eighty', 'ninety']
	hundredsStrings = ['','onehundredand','twohundredand','threehundredand', \
		'fourhundredand','fivehundredand','sixhundredand', \
		'sevenhundredand','eighthundredand','ninehundredand']
	thousandsStrings = ['','onethousand']

	teensStrings = ['ten','eleven','twelve','thirteen','fourteen','fifteen', \
		'sixteen','seventeen','eighteen','nineteen']

	if tens != 1:
		output = thousandsStrings[thousands] + hundredsStrings[hundreds] + \
			tensStrings[tens] + onesStrings[ones]
	else:
		output = thousandsStrings[thousands] + hundredsStrings[hundreds] + \
			teensStrings[ones]

	if hundreds != 0 and tens == 0 and ones == 0:
		output = thousandsStrings[thousands] + onesStrings[hundreds] + 'hundred'

	return output

longString = ''

for n in range(1,1001):
	longString += Englishify(n)

print(len(longString))

