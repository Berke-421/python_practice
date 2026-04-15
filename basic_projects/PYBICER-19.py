print("5 adet sayı girin")
depo = []

"""
old:
sayac = 0
while sayac < 5:
    try:
        c = int(input("Gir = "))

    except ValueError:
        print("Hata")
        continue

    depo.append(c)
    sayac += 1
"""

# new:
while len(depo) < 5:
    try:
        depo.append(input("Sayı gir = "))
    except ValueError:
        print("Hata")

toplam = 0
for a in depo:
    toplam += a

ortalama = toplam / len(depo)

print("Girilen sayıların toplamı: ", sum(depo))
print("Girilen en büyük sayı: ", max(depo))
print("Girilen en küçük sayı: ", min(depo))
print("Ortalama: ", ortalama)
