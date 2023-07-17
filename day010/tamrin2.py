a = input('Enter number 1: ')
f = input('Enter number 2: ')
r = int(a)
h = int(f)
for i in range(1,11):
    if i < r or i > h:
        if i % 2 ==1:
            print(i)
