def uyariVer(control):
    print("Uyarı:", control, " açı 180'den büyük olamaz")
    print("Lütfen tekrar deneyin")

a = 0; b = 0; c = 0

while True:
    a = int(input("1. açı: "))
    if a > 180:
        uyariVer("bir")
        continue

    break

while True:
    b = int(input("2. açı: "))
    if b + a > 180:
        uyariVer("iki")
        continue

    break

while True:
    c = int(input("3. açı: "))
    if a + b + c > 180:
        uyariVer("Üç")
        continue

    break

