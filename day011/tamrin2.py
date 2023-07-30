add = 0
o = input('enter number : ')
o = int(o)
for i in range(1, o):
        if i % 3 == 0:
                add = add + 1
        elif i % 5 == 0:
                add = add + 1
print(add)
