print("faktöriyel sayı hesapalama")
sayi = int(input("Sayı: ")) # Kullanıcıdan sayı al
toplam = 1 # Faktöriyel hesaplama için başlangıç değeri 1'dir.

# 1'den sayıya kadar döngü. sayi + 1 dedik çünkü range fonksiyonu son sayıyı dahil etmez. 
# Bu yüzden 1 ekledik.
for i in range(1, sayi + 1): 
    toplam *= i # Her adımda toplamı i ile çarp. i her adımda artar.

print(sayi, "! = ", toplam) # Sonucu ekrana yazdır.