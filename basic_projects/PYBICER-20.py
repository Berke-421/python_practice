print("Faktöriyel")
Sayi = None
toplam = 1

while True:
    try:
        Sayi = int(input("Sayı = "))

    except ValueError:
        print("Hata: veri doğru girilmedi")
        continue

    if Sayi < 0:
        print("Hata: faktöriyel sayı sıfırdan küçük olamaz")
        continue

    break

for a in range(1, Sayi + 1):
    toplam *= a

print(Sayi,"! =", toplam)
