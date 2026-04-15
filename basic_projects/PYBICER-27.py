import random

print("asal sayı")

depo = []
control = True

def AsalMi(n):
    if n <= 1: return  False # 1 ve kendisinden küçük olanlar asal değildir

    elif n == 2: return True # parametre 2 ise True döndür. Bu manuel bir ayardır

    elif n % 2 == 0: return False # 2 hariç çift sayılar asal değildir

    # artık tek sayılar içinden asal mı değil mi kontrolu yapılır
    c = 3 # 3'ten itibaren asal sayı kontrolu başlatacağımız için i değişkenine 3 atandı
    while c * c <= n:
        if n % c == 0:
            return False
        c += 2 # tek sayılara geçiş olacak şekilde atama olur

    return True

print("Bitirmek için: 11")
print("otomatik doldurucuyula hızlıca işlemi bitirmek için: 00")
while control:
    try:
        sayi = int(input("Sayı = "))

    except ValueError:
        print("Hata: sayı doğru girilmedi")
        continue

    if sayi == 00:
       limit = random.randint(1, 20)
       i = 0
       while i < limit:
           sayi = random.randint(0, 999)
           depo.append(sayi)
           i += 1
       control = False

    elif sayi == 11: break

    depo.append(sayi)

print(depo)
asal = {sayi for sayi in depo if AsalMi(sayi)}
print(sorted(asal))

