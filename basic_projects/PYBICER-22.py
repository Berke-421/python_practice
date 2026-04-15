import random

print("çift ve tek ayırıcı")
depo = []
depoboyutu = None

# depo boyutunun belirlendiği alan
while True:
    try:
        depoboyutu = int(input("Depo boyutunu belirleyin: "))

    except ValueError:
        print("Hata: veri doğru girilemedi, tekrar deneyin")
        continue

    break

i = 0
control = False
sayi = None
print("geriye kalan kısmı Otomatiğe almak için '00' yazın basın")

# depo içeriğini girme alanı
while i <= depoboyutu:

    if sayi == 00: control = True

    # 00 girilirse bilgisayar kendisi girecek
    if control: sayi = random.randint(1, 999)

    # 00 girilmediyse manuel girilir
    else:
        try:
            sayi = int(input("Sayı = "))

        except ValueError:
            print("Hata: veri doğru girilemedi, tekrar deneyin")
            continue

    depo.append(sayi)
    i += 1

cift = []
tek = []

for a in depo:
    if a % 2 == 0:
        cift.append(a)
    else:
        tek.append(a)

print("depo: ", depo)
print("depo uzunluğu: ", len(depo))
print("en büyük eleman: ", max(depo))
print("en küçük eleman: ", min(depo))
print("ortalama sayı: ", sum(depo) / len(depo))
print("Büyükten küçüğe sıralama: ", sorted(depo))
print()
print(len(cift), " adet çift sayı var: ", sorted(cift))
print(len(tek), " adet tek sayı var: ", sorted(tek))

