import random
# Her iki listedeki tekrar eden (aynı) elemanları bulur ve indekslerinin konumlarını gösterir

liste1 = []; liste2 = []
control1 = True; control2 = False

print("""
ikinciye listeye geçmek ve bitirmek için: x1
""")

print("Birinci liste")
while True:
    try:
        girdi = input("Girdi = ")

        if girdi.lower() == "exit":
            print("Giriş tamamlandı!")
            break

        else:
            liste1.append(int(girdi))

    except ValueError:
        print("Doğru sayı girilmedi")
        continue


for a in range(len(liste1)):
    sayi = random.randint(30, 50)
    liste2.append(sayi)

print("Liste 1: ", liste1)
print("Liste 2: ", liste2)

indeks1 = []; indeks2 = []
i = 0

tekrar_edenler1 = [deger1 for deger1 in liste1 if liste1.count(deger1) > 1]
tekrar_edenler2 = [deger2 for deger2 in liste2 if liste2.count(deger2) > 1]
toplam_tekrar = tekrar_edenler1 + tekrar_edenler2

for deger1 in liste1:
    if liste1.count(deger1) > 1:
        indeks1.append(liste1.index(deger1))
for deger2 in liste2:
    if liste2.count(deger2) > 1:
        indeks2.append(liste1.index(deger2))

while i < len(toplam_tekrar):
    print(f"{indeks1[i]} ve {indeks2[i]}, {toplam_tekrar[i]} elamanını paylaşıyor")
    i += 1
