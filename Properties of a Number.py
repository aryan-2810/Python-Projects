import random
a = int(input('Enter the starting range : '))
b = int(input('Enter the ending range : '))
c = random.randint(a,b)
print(f'Range is ({a},{b}) and the randomly picked number is {c}')
if c%2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')
if c > 0:
    print('The number is positive.')
else:
    print('The number is negative.')
flag = False
if c > 1:
    for i in range(2,c):
        if (c%i) == 0:
            flag = True
            break
    if flag:     
        print('The number is composite.')
    else:
        print('The number is prime.')
