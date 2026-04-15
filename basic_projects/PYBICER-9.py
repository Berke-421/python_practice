print("iki sayı arasındakilerin toplamını veren kod")

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))
toplam = 0

if a >= b:
    while b <= a:
        toplam += b
        b += 1

else:
    while a <= b:
        toplam += a
        a += 1

print(a, "ile", b, "arasındaki sayıların toplamı: ", toplam)