i = 1 # Sayaç değişkeni
liste = [] # Boş liste oluşturulur çünkü kullanıcıdan alınan sayılar burada saklanacak.

while i <= 5: # 5 defa döngü
    print(i, ".sayı:") # Kullanıcıya kaçıncı sayıyı girdiğini göster
    sayi = int(input("Sayi: ")) # Kullanıcıdan sayı al
    liste.append(sayi) # Alınan sayıyı listeye ekle
    i += 1 # Sayaç değişkenini 1 artır

print("En büyük sayı: ", max(liste)) # Listenin en büyük sayısını ekrana yazdır
print("En küçük sayı: ", min(liste)) # Listenin en küçük sayısını ekrana yazdır
