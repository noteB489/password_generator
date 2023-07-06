import random

print('Welcome to Your Password Generator!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
spechars = '!@#$%^&*()'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Input your passworrd length: ')
length = int(length)

print('\nHere are your passwords: ')

for pwd in range(number):
    passwords = ''
    special_char_included = False
    while len(passwords) < length or len(passwords) == 1:
        char = random.choice(chars + spechars)
        if char in spechars:
            special_char_included = True
        passwords += char
    if not special_char_included:
        passwords = ''
        for c in range(length):
            char = random.choice(chars + spechars)
            if char in spechars:
                special_char_included = True
                passwords += char
    print(passwords)