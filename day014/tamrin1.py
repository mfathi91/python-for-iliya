file_path = r"C:\files\pycharm\banana.txt"
with open(file_path, "r") as file:
    for line in file:
        int_line = int(line)
        if int_line == 5000:
            print(int_line)
