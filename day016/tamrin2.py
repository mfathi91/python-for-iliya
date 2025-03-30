bnana = r"C:\files\pycharm\banana.txt"
with open(bnana, "r") as file:
    text = file.read().lower()
    ananb = text.count("a")
    kalm = text.count("p")
    bn = text.count("d")
    print(f'a = {ananb}')
    print(f'p = {kalm}')
    print(f'd = {bn}')
    sus = bnana = ananb + kalm + bn
    print(f'total = {sus}')
