import  random

print("Sayilar girin:")
liste =[]

def rastgele():
    border = random.randint(1, 10)
    i = 0
    while i <= border:
        cc = random.randint(1, 100)
        liste.append(cc)
        i += 1

a = int(input("Ekle: "))
print("İşlem bitti")

liste.append(a)
rastgele()
liste.sort()

if liste[max(liste)] == a:
    print("You win")
    print(liste)

else:
    print("You lost")
    print(liste)