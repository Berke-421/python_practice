print("Ters Piramit\n")

h = 6

for i in range(h):
    bosluk = " " * i
    yildiz = "*" * (2 * (h - i) - 1)
    print(bosluk + yildiz)