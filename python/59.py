# Project Euler 59

def mode(sequence):
    """Finds the mode (most commonly occuring element) of a list/sequence."""
    max_count = 0
    mode_set = set()
    for entry in sequence:
        if sequence.count(entry) > max_count:
            max_count = sequence.count(entry)
    for entry in sequence:
        if sequence.count(entry) == max_count:
            mode_set = mode_set | {entry}
    return mode_set

with open("59-cipher.txt","r") as cipher_input:
    cipher = [
        int(entry) for entry in cipher_input.readline().strip('\n').split(',')
    ]

cipher_rem_0 = [cipher[j] for j in range(1201) if j % 3 == 0]
cipher_rem_1 = [cipher[j] for j in range(1201) if j % 3 == 1]
cipher_rem_2 = [cipher[j] for j in range(1201) if j % 3 == 2]

# print(mode(cipher_rem_0), mode(cipher_rem_1), mode(cipher_rem_2))
# 71, 79, 68 respectively

# print(ord(' ')) # 32

password = [71 ^ 32, 79 ^ 32, 68 ^ 32]
password_string = ''

for entry in password:
    password_string += chr(entry)

print(password_string)

message_string = ''

for j in range(len(cipher)):
    message_string += chr(cipher[j] ^ password[j % 3])

print(message_string)

the_sum = 0
for char in message_string:
    the_sum += ord(char)

print(the_sum) # 107359
