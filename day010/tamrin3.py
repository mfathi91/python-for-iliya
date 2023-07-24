a = input('Enter number 1: ')
a = int(a)
b = input('Enter number 2: ')
b = int(b)
for i in range(1,11):
    if i >= a and i <= b:
        print('bingo')
    else:
        print(i)
