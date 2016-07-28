# -*- coding: utf-8 -*-
# Project Euler 29

A = [a**b for a in range(2,101) for b in range(2,101)]

B = set(A)

print(len(B))


