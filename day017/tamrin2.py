numbers = [1, 2, 3, 4, 5, 6]
numbers2 = []
for bnana in numbers:
    if bnana % 2 == 0:
        sus = bnana * bnana
        numbers2.extend([sus])
print(numbers2)
