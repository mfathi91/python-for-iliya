bnana = r"C:\files\pycharm\banana.txt"
with open(bnana,"r") as file:
    text = file.read().lower()
    ananb = text.count("m")
    print(ananb)
