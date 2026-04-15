print("akados hesaplaması")

sayi = None
toplam = 1

while True:
    try:
        sayi = int(input("Sayı = "))

    except ValueError: # Hata durumunda kullanıcıyı uyarıyoruz
        print("Hata: doğru veri girilmedi") # Uyarı mesajı
        continue # eğer hata varsa döngünün başına dön

    break

for a in range(1, sayi + 1):
    toplam /= a

print("Sonuç = ", toplam) # Sonucu ekrana yazdırıyoruz