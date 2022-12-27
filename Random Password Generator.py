print('Hello! Welcome to password generator! \n')
import random
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_char = '!@#$%^&*()_-+=.'
chars = upper + lower + numbers + special_char
pass_len = int(input('Enter your desired password length : '))
password = ''.join(random.sample(chars,pass_len))
if pass_len >= 12:
    print('\nYour password is : ', password)
else:
    print('\nError!!\nLength should be greater than or equal to 12')
