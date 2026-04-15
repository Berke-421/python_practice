
listem = []
while True:
    giris = input("Eşya = ")
    if giris.lower() == "bitir": break
    listem.append(giris)

print([x for x in listem if listem.count(x) > 1])
