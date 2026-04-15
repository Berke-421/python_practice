import random

"""
Mimari yapı = min_değer - yoğunluklu_seçilecek_yer1 - yoğunluklu_seçilecek_yer2 - max_değer
"""

class Majority:
    def __init__(self): # yapıcı metot
        self.__maxx = None
        self.__minn = None

    # önce normal rastgele sayı seçimi için iki sayı girlir
    # sonra girilen iki sayı arasında içinden hangi aralığın daha yoğun olacağına dair iki sayi girilir
    def density_one_third(self, minn,  density1, density2, maxx):

        if minn > density1 or maxx < density2 or density1 > density2:
                 raise ValueError

        b = random.randint(1, 3) # üçte bir olasılık
        cevap = None # return edilecek değişken

        if b == 1 or b == 2: # eğer üçte iki ihtimal tutarsa
            cevap = random.randint(density1, density2) # yoğun belirtilen aralıktan sayı alınır
            return cevap

        else:
            control = True

        if control: # üçte iki tutmazsa belirtilen yoğunluk aralığı dışında sayı seçilir
            __ustVeyaAlt = random.randint(1,2) # belirtilen yoğunluğun dışında tamamen rastgele bulması için
            if __ustVeyaAlt == 1: # olasılık1 - yoğunluk1
                cevap = random.randint(minn, density1 - 1)

            else: # yoğunluk2 - olasılık2
                cevap = random.randint(density2 + 1, maxx)
        return cevap

berke = Majority()
for _ in range(20):
    sonuc = berke.density_one_third(10, 20, 40, 100)
    if 20 <= sonuc < 40:
        print(f"caught: {sonuc}")
    else:
        print(sonuc)
