print("İki adet sayı giriniz ve iki sayının arasındaki sayıların tek ve çiftlerini ayrı ayrı listeye ekleyiniz")
a = b = None
cift = []; tek = []

while True:
    try:
        a = int(input("a = "))
        b = int(input("b = "))

    except ValueError:
        print("Hata: Sayı doğru girilmedi tekrar deneyin")
        continue

    break

if a > b:
    while b < a:
        if b % 2 == 0: cift.append(b)
        elif b % 2 == 1: tek.append(b)
        b += 1

elif b > a:
    while a < b:
        if a % 2 == 0: cift.append(a)
        elif a % 2 == 1: tek.append(a)
        a += 1

elif a == b: print("a ve b eşit! Yani ara sayılar 0")

print(a, "ile", b, " arası sayılardan çift olanları: ")
print(cift)

print("-----------------------------------------------------------")

print(a, "ile", b, " arası sayılardan tek olanları: ")
print(tek)