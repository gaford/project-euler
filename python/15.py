# -*- coding: utf-8 -*-
# Project Euler 15

# start = (0,0)
# grid = (20,20)
# paths = [[(0,0)]]

# def nextSteps(path):
# 	# takes a list path of points (x,y)
# 	lastPoint = path[-1]
# 	if lastPoint != grid:
# 		path1 = []
# 		path2 = []
# 		if lastPoint[0] < grid[0]:
# 			path1 = path + [(lastPoint[0] + 1, lastPoint[1])]
# 		if lastPoint[1] < grid[1]:
# 			path2 = path + [(lastPoint[0], lastPoint[1] + 1)]
# 		return list(filter(None,[path1, path2]))
# 	else:
# 		return [path]

# print(len(paths))

# def CountPaths(a,b):
# 	grid = (a,b)
# 	N = 0
# 	start = [(0,0)]
# 	finish = []
# 	while len(start) > 0:
# 		cache = []
# 		for j in range(len(start)):
# 			if start[j][0] < grid[0] - 1 and start[j][1] < grid[1] - 1:
# 				cache.append((start[j][0]+1,start[j][1]))
# 				cache.append((start[j][0],start[j][1]+1))
# 			elif start[j][0] == grid[0] - 1 and start[j][1] < grid[1] - 1:
# 				# finish.append((grid[0],start[j][1]))
# 				N += 1
# 				cache.append((grid[0] - 1,start[j][1] + 1))
# 			elif start[j][0] < grid[0] - 1 and start[j][1] == grid[1] - 1:
# 				cache.append((start[j][0]+1,grid[1] - 1))
# 				# finish.append((start[j][0],grid[1]))
# 				N += 1
# 			else:
# 				# finish.append((start[j][0],grid[1]))
# 				# finish.append((grid[0],start[j][1]))
# 				N += 2
# 		start = cache
# 	return N

# for j in range(1,11):
# 	print("%s by %s grid:  %s paths" % (j,j,CountPaths(j,j)))

from math import *

# the formula is the middle binomial coefficient 2N choose N

print(factorial(40) // ( factorial(20)**2))

# see the solutions for many useful techniques

