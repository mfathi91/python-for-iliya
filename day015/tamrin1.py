file_path = r"C:\files\pycharm\banana.txt"
with open(file_path, "r") as file:
    for line in file:
        int_line = int(line)
        if int_line % 2 == 0:
            print(f" {int_line} is even")
        elif int_line % 2 == 1:
            print(f"{int_line} is odd ")
