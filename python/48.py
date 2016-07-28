# -*- coding: utf-8 -*-
# Project Euler 48

summands = [pow(n,n,10**10) for n in range(1,1001)]

print(sum(summands) % 10**10) # 9110846700

