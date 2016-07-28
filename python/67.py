# Project Euler 67

# Process the file

with open('67-triangle.txt','r') as inputFile:
    rawData = list(inputFile)

for j in range(len(rawData)):
   rawData[j] = rawData[j].replace('\n',' ')
rawData[-1] += ' '

triangle = [[] for __ in range(len(rawData))]

for j in range(len(rawData)):
    for k in range(len(rawData[j]) // 3):
        triangle[j].append(
            int(rawData[j][3*k : 3*k + 2])
            )

# Build a triangle to test for the maximum path.  Proceed by starting at the
# next-to-last row and adding the value of the maximum allowable choice on
# the final row.  Proceed iteratively upwards.  The answer will be the entry
# at the top of the triangle.

path_triangle = triangle

for j_inv in range(0,99):
    j = 98 - j_inv
    for k in range(len(triangle[j])):
        path_triangle[j][k] += \
            max(path_triangle[j+1][k], path_triangle[j+1][k+1])

print(path_triangle[0][0])
