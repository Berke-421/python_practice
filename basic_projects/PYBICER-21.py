print("Hesap makinesi") # Basit bir hesap makinesi uygulaması

control = None 
sayac = 1

def girdi1(aa = 1):
    while True:
        try:
            tercih = int(input("sayı = "))
            aa = tercih

        except ValueError:
            print("Hata: Sayı doğru girilmedi")
            continue
        break

    return aa

print("-" * 15, sayac, "-" * 15)
while True:
    a = girdi1()

    while True:
        tur = input("İşlem türü seçin: (+, -, *, /) = ")
        match tur:
            case "+":
                control = 1

            case "-":
                control = 2

            case "*":
                control = 3

            case "/":
                control = 4

            case _:
                print("Doğru işlem türü girilmedi")
                continue

        break

    b = girdi1()
    toplam = 0

    match control:
        case 1:
            toplam = a + b

        case 2:
            toplam = a - b

        case 3:
            toplam = a * b

        case 4:
            if b == 0:
                print("payda sıfır olamaz")
                print("Sonuc çözüm kümesi: Tanımsız")
            else:
                toplam = a / b

    sayac += 1

    print("Sonuc = ", toplam)
    print("-" * 15, sayac, "-" * 15)


