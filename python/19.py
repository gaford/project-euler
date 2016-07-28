# -*- coding: utf-8 -*-
# Project Euler 19

# 1 Jan 1901 was a Tuesday

Year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

TimePeriod = (Year * 3 + LeapYear) * 24 + Year * 4


dayTicker = 0 # adding one for each day; first day is a Tues, so need to add
Sundays = 0
for month in TimePeriod:
	for day in range(1,month+1):
		dayTicker += 1
		if day == 1 and dayTicker % 7 == 6:
			Sundays += 1

print(dayTicker)
print(Sundays)

# 171 is the number of Sundays occuring on the first of the month