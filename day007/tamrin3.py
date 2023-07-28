add = 0
o = input('enter number 1: ')
y = input('enter number 2: ')
o = int(o)
y = int(y)
for i in range(o, y):
    if i % 5 == 0:
        add = add + 1
print(add)
