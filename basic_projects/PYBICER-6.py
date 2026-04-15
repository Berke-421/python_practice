def mesaj(aa, bb = "sıfır"):
    print("a", aa, "ve", bb ,"bir sayıdır")

a = int(input("a = "))

if a % 2 == 0 and a > 0: mesaj("çift", "pozitif")

elif a % 2 != 0 and a < 0: mesaj("tek", "negatif")

elif a % 2 != 0 and a > 0: mesaj("tek", "pozitif")

elif a % 2 == 0 and a < 0: mesaj("çift", "negatif")

else:
    mesaj("çift")

