a = input('Enter number 1: ')
b = input('Enter number 2: ')
f = int(a)
g = int(b)
if f % 2 == 0:
    print(f + g)
    print(f - g)
elif f % 2 == 1:
    print(f * g)
    print(f / g)
print('Thank you')
