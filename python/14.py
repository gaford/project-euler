# -*- coding: utf-8 -*-
# Project Euler 14

# generating the Collatz sequence starting with a positive integer N
def Collatz(N):
	output = [N]
	while output[-1] != 1:
		if output[-1] % 2 == 0:
			output.append(int(output[-1]/2))
		else:
			output.append(3*output[-1]+1)
	return output

def reverseCollatz(N):
	output = [[1]]
	for j in range(N):
		subOutput = []
		for entry in output[j]:
			subOutput.append(2*entry)
			if entry % 6 == 4 and entry != 4:
				subOutput.append(int((entry-1)/3))
		output.append(subOutput)
	return output

ourRange = range(2,1000000)
lengths = [len(Collatz(j)) for j in ourRange]

print(lengths.index(max(lengths))) # 837797

# so the starter for the longest sequence is 837799