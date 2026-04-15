import math
from Bagımsız.oop_projeleri.fractional_and_nonfractional_floats import AutonumberFloatAndInt

class Silindir:
    __berke = AutonumberFloatAndInt()
    __kutle = None

    def __init__(self,yaricap,yukseklik):
        try:
            self.yaricap = float(yaricap)
            if yaricap <= 0:
                raise ValueError
        except ValueError:
            print("Doğru yarıçap girilmedi")
            self.yaricap = self.__berke.oneinthreechanceForFloat(1,90)

        try:
            self.yukseklik = yukseklik
            if yukseklik <= 0:
                raise ValueError
        except ValueError:
            print("Doğru yükseklik girilmedi")
            self.yukseklik = self.__berke.oneinthreechanceForFloat(1,300)

    def tabanalani(self):
        cevap = math.pi * math.pow(self.yaricap, 2)
        return cevap

    def hacim(self):
        taban = self.tabanalani()
        cevap = taban * self.yukseklik
        return cevap

    def yanalalan(self):
        cevap = 2 * math.pi * self.yaricap * self.yukseklik
        return cevap

    def tabancevresi(self):
        cevap = 2 * math.pi * self.yaricap
        return cevap

    def toplamyuzeyalan(self):
        cevap = 2 * math.pi * math.pow(self.yaricap, 2) + 2 * math.pi * self.yaricap * self.yukseklik
        return cevap

    def cap(self):
        d = 2 * self.yaricap
        return d

    def caprazuzunluk(self):
        d = math.pow(self.yukseklik, 2) + math.pow(2*self.yaricap, 2)
        cevap = math.sqrt(d)
        return cevap

    def kutlehesabi(self, p):
        try:
            yogunluk = int(p)
            if yogunluk <= 0:
                raise ValueError

        except ValueError:
            print("Yoğunluk doğru girilmedi")
            yogunluk = self.__berke.oneinthreechanceForFloat(1, 50)

        m = yogunluk * self.hacim()
        return m

    def ataletmomenti(self, p):
        self.__kutle = self.kutlehesabi(p)
        i = self.__kutle * math.pow(self.yaricap, 2) / 2
        return i


