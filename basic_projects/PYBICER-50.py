import random
# Her iki listedeki tekrar eden (aynı) elemanları bulur ve indekslerinin konumlarını gösterir

liste1 = []; liste2 = []
control1 = True; control2 = False

print("""
ikinciye listeye geçmek ve bitirmek için: x1
""")

print("Birinci liste")
while True:
    try:
        girdi = input("Girdi = ")

        if girdi.lower() == "exit":
            print("Giriş tamamlandı!")
            break

        else:
            liste1.append(int(girdi))

    except ValueError:
        print("Doğru sayı girilmedi")
        continue


for a in range(len(liste1)):
    sayi = random.randint(30, 50)
    liste2.append(sayi)

print("Liste 1: ", liste1)
print("Liste 2: ", liste2)

