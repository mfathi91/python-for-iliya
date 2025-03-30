bnana = r"C:\files\pycharm\banana.txt"
with open(bnana, "r") as file:
    text = file.read().lower()
    ananb = text.count("a")
    kalm = text.count("p")
    bn = text.count("d")
    sus = bnana = ananb + kalm + bn
    print(sus)
