sozluk = {

    "Berke": "Adamolan",
    "Dost": "gerzek",
    "ayşe": "zekiveçalışkan",
    "zırdeli": "maltoros",
    "atakan": "manyakvedeli",
    "çekirdek": "yemekçıtlamak",
    "a" : "nasılsınbakalımumarımhayatıniyidiradam",
    "s": "a"
}

uzunluk = {}
sayac = 1; sayac2 = 0
while sayac <= len(sozluk.keys()):
    a = str(sayac)
    numara_belirtisi = a + ".kelime uzunluk: "
    deger = list(sozluk.values())

    uzunluk.setdefault(
        numara_belirtisi, len(deger[sayac2])
    )
    sayac += 1
    sayac2 += 1

print(uzunluk)