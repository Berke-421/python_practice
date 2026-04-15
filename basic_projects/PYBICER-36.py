import math

def sayigiris():
    while True:
        try:
            sayii = int(input("Sayı === "))
            return sayii

        except ValueError:
            print("Hata: Lütfen sayı giriniz")
            continue



class Matematik:
    _pi = 3.14

    def __init__(self, sayi1):
        self.sayi1 = sayi1
        self.depo = []

    def kareal(self):
       return  math.pow(self.sayi1, 2)

    def derecesinial(self, sayi2):
        return math.pow(self.sayi1, sayi2)

    def karekokunual(self):
        return math.sqrt(self.sayi1)

    def topla(self, sayi2):
        return self.sayi1 + sayi2

    def cikar(self, sayi2):
        return  self.sayi1 - sayi2

    def carp(self, sayi2):
        return self.sayi1 * sayi2

    def bol(self, sayi2):
        if sayi2 == 0:
            print("Hata: payda sıfır olamaz o yüzden sonuç TANIMSIZDIR")

        else:
            return self.sayi1 / sayi2


tekrar = False
while True:
    print("sayıyı giriniz ve İşleminizi seçiniz: ")
    sayiniz = sayigiris()
    sonuc = None
    nesne = Matematik(sayiniz)

    print(f"""

    {sayiniz} ile yapılabilecek işlemler:

    1-kare al
    2-derecesini al
    3-kare kökükünü al
    4-topa
    5-çıkar
    6-çarp
    7-böl

    Not: Sonlandırmak için 8 sayısına basıp enter deyiniz
    Not: Başka sayı üzerinden işlem için 9 basıp enter deyiniz

    """)

    sayac = 0
    akis = True
    while akis:

        tercih = sayigiris()
        match tercih:
            case 1:
                sonuc = nesne.kareal()
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 2:
                print(f"{sayiniz} sayısının alıncağı (x) kuvveti belirleyin")
                x = sayigiris()
                sonuc = nesne.derecesinial(x)
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 3:
                sonuc = nesne.karekokunual()
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 4:
                print(f"{sayiniz} hangi sayı ile toplanacak")
                x1 = sayigiris()
                sonuc = nesne.topla(x1)
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 5:
                print(f"{sayiniz} hangi sayı ile çıkarılacak")
                x1 = sayigiris()
                sonuc = nesne.cikar(x1)
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 6:
                print(f"{sayiniz} hangi sayı ile çarpılacak")
                x1 = sayigiris()
                sonuc = nesne.carp(x1)
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 7:
                print(f"{sayiniz} hangi sayı ile bolunecek")
                x1 = sayigiris()
                sonuc = nesne.bol(x1)
                print(f"Sonucunuz: {sonuc}")
                sayac = 0

            case 8:
                akis = False
                print("İşlem sona erdi")

            case 9:
                akis = False

            case _:
                sayac += 1
                if sayac % 3 == 0:
                    print("""

                    1-kare al
                    2-derecesini al
                    3-kare kökükünü al
                    4-topa
                    5-çıkar
                    6-çarp
                    7-böl

                    """)
                else:
                    print("Doğru tercih girilmedi")


    if tekrar: continue
    else: pass
