sozluk = {

    "Türkiye" : "Ötüken",
    "Almanya" : "Berlin",
    "Çin" : "Pekin",
    "Amerika" : "Washington D.C.",
    "Fransa" : "Paris",
    "Rusya" : "Moskova",
    "İran" : "Tahran",
    "Japonya" : "Tokya"
}

print(f"Sözlüğün anahtarlar türü: {sozluk.keys()}")

for keys in sozluk.keys():
    print(keys)

for value in sozluk.values():
    print(value)