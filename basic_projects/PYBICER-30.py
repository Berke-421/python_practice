import random

print("Tekrar bulucu")

depo = list() # depo oluşturduk
control = True
gir = None

print("İşleme son vermek için '00' yazın")
print("Otomatiğe almak için '11' yazın")

while True:

    if control:
        try:
            gir = int(input("Sayı = "))
            if gir == 00: break

            elif gir == 11:
                control = False

            else: depo.append(gir)

        except ValueError:
            print("Hata: sayı doğru girilmedi, lütfen tekrar deneyiniz")
            continue

    else:
        limit = random.randint(1, 10)
        i = 0

        while i <= limit:
            gir = random.randint(0, 999)
            depo.append(gir)
            i += 1
        break


print(depo)
tekrar_eden = [x for x in depo if depo.count(x) > 1 ]
print("Tekrar eden sayılar: ", tekrar_eden)

