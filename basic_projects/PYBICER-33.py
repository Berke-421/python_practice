import random

print("Tek sayı ayıklama")
depo = []
girdi = None

print("Bitirmek için '00' ")
print("otomatik tamamlamak için '11' ")

while True:
    try:
        girdi = int(input("Sayi = "))

        if girdi == 0:
            break

        elif girdi == 1:
            limit = random.randint(1, 20)
            olasilik = [1, 1, 1, 1, 5, 5, 5, 7, 7]
            i = 0
            while i < limit:

                depo.append(random.randint(1,300))
                i += 1
            break

        depo.append(girdi)

    except ValueError:
        print("Hata: doğru sayı girilmedi, tekrar deneyin")
        continue

tek = [teksayi for teksayi in depo if teksayi % 2 != 0]
print("Mevcut depo: ", depo)
print("Tek sayilar: ", tek)