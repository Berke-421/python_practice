print("Hesap makinesi") # Basit bir hesap makinesi uygulaması

sayac = 1 # sayaç değişkeni her işlemden sonra artacak çünkü işlem numarasını gösteriyor ve kullanıcıya kolaylık sağlıyor
# ne kadar işlem yapıldığını gösteriyor

def girdi1(aa = 1): # Profesyonel bir şekilde sayı girişi almak için fonksiyon tanımladık 
    while True:  # Döngü ile kullanıcı doğru sayı girene kadar tekrar tekrar soracağız
        try: # Hata yakalama bloğu
            return  float(input("Sayı gir: ")) # return burada döngüyü bitirebilir ve fonksiyondan çıkabiliriz

        except ValueError: # Hata türü
            print("Hata: Sayı doğru girilmedi") # Hata mesajı
            continue # Döngünün başına dönüyor EĞER HATA VARSA

print("-" * 15, sayac, "-" * 15) # İşlem numarasını gösteren çizgi kullancıya kolaylık sağlıyor
while True: # Ana döngü 
    a = girdi1() # Birinci sayıyı alıyoruz

    tur = input("İşlem türü (+ - * /): ") # İşlem türünü alıyoruz 
    while tur not in ["+", "-", "*", "/"]: # liste içinde istenilen işlemler olmazsa tekrar sor 
        print("Hata: Doğru işlem türü girilmedi") # Hata mesajı 
        tur = input("İşlem türü (+ - * /): ") # Tekrar işlem türünü alıyoruz

    b = girdi1() # İkinci sayıyı alıyoruz
    toplam = None # Sonucu tutacak değişken

    match tur: # İşlem türüne göre işlemi yapıyoruz
        case "+": # Eğer işlem türü toplama ise
            toplam = a + b # Toplama işlemi yapılıyor

        case "-": # Eğer işlem türü çıkarma ise
            toplam = a - b # Çıkarma işlemi yapılıyor
        case "*": # Eğer işlem türü çarpma ise
            toplam = a * b # Çarpma işlemi yapılıyor

        case "/": # Eğer işlem türü bölme ise
            if b == 0: # Payda sıfır ise hata mesajı veriyoruz
                print("Hata: payda sıfır olamaz") # Hata mesajı
                print("Sonuc çözüm kümesi: Tanımsız") # sonuç kullanıcıya gösteriliyor
            else: # Payda sıfır değilse bölme işlemi yapılıyor
                toplam = a / b # Bölme işlemi yapılıyor

    sayac += 1 # döngü sonunda sayaç 1 artırılıyor
    print("Sonuc = ", toplam) # Sonuç ekrana yazdırılıyor
    print("-" * 15, sayac, "-" * 15) # İşlem numarasını gösteren çizgi kullancıya kolaylık sağlıyor
