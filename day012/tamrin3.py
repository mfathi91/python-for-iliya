add_m = 0
add_a = 0
string = input('Enter a String: ')

for i in string:
    if i == 'm':
        add_m = add_m + 1
    elif i == 'a':
        add_a = add_a + 1

if add_m > add_a:
    print('m')
elif add_a > add_m:
    print('a')
else:
    print('banananananana')
