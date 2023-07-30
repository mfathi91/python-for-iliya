o = input('enter number : ')
o = int(o)
for i in range(1, o):
    if i % 4 == 0:
        print(f'{i} - yes')
    else:
        print(f'{i} - no')
