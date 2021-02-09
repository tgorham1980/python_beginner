

def create_phone_number(n):
    n = str(n)
    for [i] in n:
        frogger = n.replace(",", "")
        pacman = frogger.replace("[", "").replace("]", "").replace(" ", "")
    galaga1 = pacman[0:3]
    galaga2 = pacman[3:6]
    galaga3 = pacman[6:10]
    galaga4 = "(" + galaga1 + ")" + " " + galaga2 + "-" + galaga3
    return galaga4.rstrip()

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))



