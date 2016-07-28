# Project Euler 62

N = 10**4

cubes = [n**3 for n in range(N)]

def digit_count(x):
    string = str(x)
    count_0 = string.count('0')
    count_1 = string.count('1')
    count_2 = string.count('2')
    count_3 = string.count('3')
    count_4 = string.count('4')
    count_5 = string.count('5')
    count_6 = string.count('6')
    count_7 = string.count('7')
    count_8 = string.count('8')
    count_9 = string.count('9')
    return (
        count_0, count_1, count_2, count_3, count_4, count_5,
        count_6, count_7, count_8, count_9
    )

cube_digits = {}

for cube in cubes:
    try:
        cube_digits[digit_count(cube)].append(cube)
    except KeyError:
        cube_digits[digit_count(cube)] = [cube]

cube_digits_keys = list(cube_digits.keys())

for key in cube_digits_keys:
    if len(cube_digits[key]) == 5:
        print(cube_digits[key])

# 127035954683
