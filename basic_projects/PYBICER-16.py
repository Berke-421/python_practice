print("İki adet sayı")
a = b = sonuc = None
control = False

while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))

    except ValueError:
        print("Hata: sayı geçersiz")
        continue

    break

print("hesaplama türü: ")
print("""

1.Topla
2.Çıkar
3.Çarp
4.Böl

Not: İptal etmek için \"x\" tuşuna basınız
""")

while True:
    tercih = input("Tercih: ")

    if tercih == "1": sonuc = a + b
    elif tercih == "2": sonuc = a - b
    elif tercih == "3": sonuc = a * b

    elif tercih == "4":
        if b == 0:
            print("Bölme işlemi tamamlanamadı: b sayısı bölme işleminde 0 olamaz")
            control = True

        else:
            sonuc = a / b

    elif tercih == "x":
        break

    else:
        print("Tercih doğru girilmedi")
        continue

    break

if control: print("Sonuç = Tanımsız")
else: print("Sonuç = ", sonuc)
