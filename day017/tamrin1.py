bnana = r"C:\files\pycharm\banana.txt"
with open(bnana,"r") as file:

        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()
        line4 = file.readline()
        print(f'line1 = {line1}')
        print(f'line2 = {line2}')
        print(f'line3 = {line3}')
        print(f'line4 = {line4}')
