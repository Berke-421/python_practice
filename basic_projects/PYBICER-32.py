def sayac(kelime):
    kelime = kelime.replace(" ", "")
    return len(kelime)

girdi = input("Kelime girin: ")

print("Girilen kelime uzunluğu: ", sayac(girdi))
