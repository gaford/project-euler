# -*- coding: utf-8 -*-
# Project Euler 25

def FibonnaciSeries(N):
	series = [1,1]
	for j in range(2,N):
		series.append(series[-1] + series[-2])
	return series

FibStringSeries = [str(x) for x in FibonnaciSeries(10000)]

j = 0
while len(FibStringSeries[j]) < 1000:
	j += 1
else:
	print(j+1)
