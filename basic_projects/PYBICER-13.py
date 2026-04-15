i = 1 # Sayaç değişkeni
liste = [] # Boş liste oluşturulur çünkü kullanıcıdan alınan sayılar burada saklanacak.

while i <= 5: # 5 defa döngü
    print(i, ".sayı:") # Kullanıcıya kaçıncı sayıyı girdiğini göster
    sayi = int(input("  ")) # Kullanıcıdan sayı al
    liste.append(sayi) # Alınan sayıyı listeye ekle
    i += 1 # Sayaç değişkenini 1 artır

toplam = sum(liste) # Listenin tüm sayılarını topla
print("Toplam = ", toplam) # Toplamı ekrana yazdır