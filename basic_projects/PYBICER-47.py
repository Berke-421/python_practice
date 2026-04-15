ana_liste = [[]]
sayac = 1
mini_sayac = 1
control = True

print("Liste içinde liste oluşturma aracı")
print("listeyi bitirmek Bitirmek için x1 yazınız")
print("işlemi tamamen bitirmek için y1 yazınız")

while control:
    print(f"{sayac}.listenin değerleri")

    while True:
        print(f"{mini_sayac}. değer")
        deger = input("girdi = ")

        if deger == "x1" or deger == "X1":
            print(f"{sayac}. liste tamamlandı")
            mini_sayac = 1
            break

        if deger == "y1" or deger == "Y1":
            print("ana liste tamamlandı")
            control = False
            break

        ana_liste.append([].append(deger))
        mini_sayac += 1

    sayac += 1

del ana_liste[0]

print("Ana liste: ", ana_liste)
print(f"{len(ana_liste)} adet liste içeriyor")
print(f"en uzun liste: ", max(ana_liste, key=len))
print(f"en kısa liste: ", min(ana_liste, key=len))