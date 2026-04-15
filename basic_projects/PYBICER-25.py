print("Notmatik")

ogrenci = []
nott = []
sayac = 1
sayac2 = 0

print("Öğrenci adlarını girin")
print("İşleme son vermek için 0 tuşuna basın")

while True:
    print(sayac, ". öğrenci")
    isim = input("Öğrenci ismi = ")

    if isim == '0':
        print("Öğrenci isimleri tamamlandı")
        break

    if any(a.isdigit() for a in isim):
        print("Hata: öğrenci isminde sayı olamaz")
        print("İsmi tekrar girin")
        continue

    ogrenci.append(isim)
    sayac += 1

while sayac2 < len(ogrenci):
    try:
        print(ogrenci[sayac2], "Öğrencisinin notu")
        notu = int(input("Not = "))

        if notu > 100 or notu < 0:
            print("Notlar 0-100 arası olmak zorunda")
            continue

        nott.append(notu)
        sayac2 += 1

    except ValueError:
        print("Hata: Not doğru girilmedi")
        continue

not_sozluk = dict(zip(ogrenci, nott))
print(not_sozluk)
