# Project Euler 79

with open('79-keylog.txt','r') as input_file:
    keylog = list(input_file)

for j in range(len(keylog)):
    keylog[j] = keylog[j].replace('\n','')

first_digits = set()
second_digits = set()
third_digits = set()

for j in range(50):
    first_digits = first_digits | {int(keylog[j][0])}
    second_digits = second_digits | {int(keylog[j][1])}
    third_digits = third_digits | {int(keylog[j][2])}

# print(first_digits) # 7 appears only here
# print(second_digits)
# print(third_digits) # 0 appears only here

# print(first_digits & second_digits) # 3 never a last digit

# print(second_digits & third_digits) # 9 never a first digit

# print(first_digits & second_digits & third_digits)

seven_is_first_digit = set()
for item in keylog:
    if item[0] == '7':
        seven_is_first_digit = seven_is_first_digit | {int(item[1:])}

zero_is_last_digit = set()
for item in keylog:
    if item[-1] == '0':
        zero_is_last_digit = zero_is_last_digit | {int(item[:2])}

# print(seven_is_first_digit) # 3 > 1 > 6 > 2 > 8 > 9
# print(zero_is_last_digit)

# 73162890
