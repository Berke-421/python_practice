import  random

print("Sayilar girin:")
liste =[]

def rastgele(): # rastgele sayılar ekleyen fonksiyon
    border = random.randint(1, 10) # 1 ile 10 arasında rastgele bir sayı belirliyoruz
    for _ in range(border): # belirlenen sayı kadar döngü oluşturuyoruz. _ dedik çünkü döngü sayısını kullanmayacağız
        liste.append(random.randint(1, 100)) # 1 ile 100 arasında rastgele sayılar ekliyoruz

a = int(input("Ekle: ")) # kullanıcıdan bir sayı alıyoruz
print("İşlem bitti") # işlem bitti mesajı

liste.append(a) # kullanıcıdan alınan sayıyı listeye ekliyoruz
rastgele() # rastgele sayılar ekliyoruz
liste.sort() # listeyi sıralıyoruz

# max fonksiyonu bir liste içindeki en büyük sayıyı bulur
# max nerelerde kullanılırsa orada en büyük sayıyı döndürür

if max(liste) == a: # max fonksiyonu ile en büyük sayıyı bulup a'ya eşit mi diye kontrol ediyoruz
    print("You win")
    print(liste)

else: # eğer a en büyük sayı değilse
    print("You lost")
    print(max(liste)) # en büyük sayıyı yazdırıyoruz