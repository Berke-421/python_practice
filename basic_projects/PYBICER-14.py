import random # Rastgele sayı üretmek için random modülünü ekliyoruz

print("1-100 arası sayı tahmin etme oyunu") # Oyun hakkında bilgi veriyoruz
control = True # Oyun başlangıcı kontrol değişkeni çünkü oyun tekrar oynanabilir olacak

while True: # Oyun döngüsü
    can = 3 # Başlangıç can sayısı 3
    tahmin = 0  # başta tahmin değeri 0 olarak ayarlanıyor çünkü kullanıcıdan giriş alınacak
    sayi = random.randint(1, 100) # 1 ile 100 arasında rastgele bir sayı seçiyoruz

    if control: print("Oyun başladı!") # Oyun ilk kez başlıyorsa bu mesajı göster
    else: print("Oyun tekrar başladı!") # Oyun tekrar başlıyorsa bu mesajı göster

    while can > 0: # Can 0 olana kadar devam et yoksa oyun biter
        try: # hata kontrolü yapıyoruz
            tahmin = int(input("Tahmin et = ")) # Kullanıcıdan tahmin al

        except ValueError: # Hata durumunda kullanıcıyı uyarıyoruz
            print("Lütfen bir sayı girin") # Uyarı mesajı
            continue # eğer hata varsa döngünün başına dön

        if tahmin == sayi: # Doğru tahmin durumu
            print("-" * 20) # okuma kolaylığı için çizgi çekiyoruz
            print("Kazandın!")
            print("Şu kadar canın kalmıştı: ", can) # Kalan can sayısını göster
            print("-" * 20)
            break # Doğru tahmin yapıldıysa döngüden çık

        else: # Yanlış tahmin durumu
            can -= 1 # Can sayısını bir azalt eğer yanlışsa

            print("-" * 20)
            print("Yanlış tahmin")
            if tahmin > sayi: print("Daha küçük bir sayı dene") # Kullanıcıya ipucu ver
            if tahmin < sayi: print("Daha büyük bir sayı dene") # Kullanıcıya ipucu ver2
            print("Canın: ", can) # mevcut can sayısını göster
            print("Tekrar dene")
            print("-" * 20)

    if can == 0: # Can bittiğinde oyunu kaybetme durumu
        print("Kaybettin")
        print("Bilgisayarın tahmin ettiği sayı: ", sayi) # mevcut sayıyı göster

    ea = str(input("Tekrar oynamak ister misin? (E/A)")).upper() # Kullanıcıya tekrar oynama sorusu

    if ea == "H": # Kullanıcı oyunu bitirmek isterse
        print("Oyun bitti")
        break # Döngüden çık yani oyunu sonlandır

    elif ea == "E": # Kullanıcı tekrar oynamak isterse
        control = False # Oyun tekrar başladığında farklı mesaj vermek için kontrol değişkenini False yap
        continue # Döngünün başına dön
