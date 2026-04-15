print("PINAR")
print("Zeldodria And Duxnei")
print("""

Başlamak için:
c: Başla
s: ayarlar
d: yapımcılar
x: Çıkış
""")


while True:
    tercih = input("Seçiniz = ").lower()

    if tercih == "c":
        print("Oyun başlıyor")

    elif tercih == "s":
        print("Ayarlar")

    elif tercih == "d":
        print("Pinar: A game by Berke Bicer")

    elif tercih == "x":
        print("Oyun kapanıyor")

    else:
        print("Doğru tuşa basılmadı: Tekrar deneyiniz")
        continue

    break

