bozorgtarin = 0
file_path = r"C:\files\pycharm\banana.txt"
with open(file_path, "r") as file:
    for line in file:
        int_line = int(line)
        if int_line > bozorgtarin:
            bozorgtarin = int_line
print(bozorgtarin)
