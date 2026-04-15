print("iki sayı arasındakilerin toplamını veren kod")

a = int(input("İlk sayı = ")) # kullanıcıdan ilk sayıyı alır
b = int(input("İkinci sayı = ")) # kullanıcıdan ikinci sayıyı alır
toplam = 0 # toplam değişkenini başlatır

if a >= b: # a büyükse çünkü artan sırayla toplama yapacağız
    for i in range(b, a + 1): toplam += i # b'den a'ya kadar olan sayıları toplar

else: # b büyükse
    for i in range(a, b + 1): toplam += i # a'dan b'ye kadar olan sayıları toplar


print(a, "-", b, "arasındaki sayıların toplamı: ", toplam) # sonucu yazdırır