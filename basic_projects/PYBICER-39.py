giris1 = input("1.girdi = ")

if giris1.isupper():
    giris1 = giris1.lower()
    print("Düzeltildi: ", giris1)

elif giris1.islower():
    giris1 = giris1.upper()
    print("Düzeltildi: ", giris1)

else:
    giris2 = ""
    for a in giris1:
        if a.islower(): a = a.upper()
        elif a.isupper(): a = a.lower()
        giris2 += a

    print(giris2)