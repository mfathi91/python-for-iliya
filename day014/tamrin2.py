file_path = r"C:\files\pycharm\banana.txt"
with open(file_path, "r") as file:
    for line in file:
        add = 0
        for harf in line:
            if harf == 'm':
                add = add + 1
        print(f'{line.strip()}: {add}')
