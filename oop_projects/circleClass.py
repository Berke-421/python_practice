import math
from Bagımsız.oop_projeleri.fractional_and_nonfractional_floats import AutonumberFloat

class Circle:
    __pi = math.pi
    __daire_derecesi = 360
    __rastgele = AutonumberFloat()

    def __init__(self, r, aci):
        try:
            self.r = float(r) # parametre floata çevrilir
            if self.r < 0: # eğer yarıçap eksi girilirse:
                raise ValueError # hata fırlatılır
        except ValueError:
            print("yarıçap doğru girilmedi, başka yarıçap atandı")
            self.r = self.__rastgele.maybe_float_one_third(1, 100)

        try:
            self.aci = float(aci) # parametre floata çevrilir
            if self.aci < 0: # eğer yarıçap eksi girilirse:
                raise ValueError # hata fırlatılır
        except ValueError:
            print("Doğru açı girilmedi başka açı atandı")
            self.aci = self.__rastgele.oneinthreechanceForFloat(1,360)

    def __bol(self, girdi, cikti):
        if cikti == 0:
            return "Hata: payda sıfır olamaz"
        else:
            return girdi / cikti

    def alan_hesapla(self, goster=False):
        alan = self.__pi * math.pow(self.r, 2)
        if goster:
            print("Alan = ", alan)
        else:
            return alan

    def cevre_hesapla(self, goster=False):
        cevre = 2 * self.__pi * self.r
        if goster:
            print("Çevre = ", cevre)
        else:
            return cevre

    def tarali_alan(self, goster=False):
        ust = self.__pi * math.pow(self.r, 2) * self.aci
        tarali = self.__bol(ust, 360)
        if goster:
            print("Taralı alan = ", tarali)
        else:
            return tarali

print("-" * 35)

berke = Circle(12, 56)
berke.alan_hesapla(True)
berke.cevre_hesapla(True)
berke.tarali_alan(True)

print("-" * 35)

bicer = Circle(50, "we")
print(bicer.aci)
print(bicer.r)
print(bicer.alan_hesapla())
print(bicer.cevre_hesapla())
print(bicer.tarali_alan())

print("-" * 35)