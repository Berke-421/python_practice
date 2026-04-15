import random

liste1 = []
liste2 = []
sayac = 0

print("5 adet sayı giriniz")
while sayac < 5:
    try:
        girdi = int(input("Sayı = "))
        liste1.append(girdi)
        sayac += 1

    except ValueError:
        print("Hata: doğru veri tipi girilmedi")
        continue

sayac = 0
while sayac < 5:
    liste2.append(random.randint(0, 100))
    sayac += 1

carp = []

i = 0
while i < 5:
    sonuc = liste1[i] * liste2[i]
    carp.append(sonuc)
    i += 1

print(carp)