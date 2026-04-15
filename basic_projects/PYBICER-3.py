a = int(input("a = "))
b = int(input("b = "))
c = 0

print("topla: 1, çıkart: 2, çarp: 3, böl: 4")

while True:
    tercih = str(input("İşlem: "))

    if tercih == "1":
        c = a + b
        print("a + b = ", c)
        print(type(c))
        break

    elif tercih == "2":
        c = a - b
        print("a - b = ", c)
        print(type(c))
        break

    elif tercih == "3":
        c = a * b
        print("a * b = ", c)
        print(type(c))
        break

    elif tercih == "4":
        c = a / b
        print("a / b = ", c)
        print(type(c))
        break

    else:
        print("Hata: Tercih girilmedi")
        continue