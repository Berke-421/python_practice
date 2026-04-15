class Hesap: # parent class
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def bilgi_ver(self):
        print("Hesap Türü bilinmiyor")

    def hesapla(self):
        raise NotImplementedError("İşlemi uygulamadın mal")

class Topla(Hesap): # child class
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def bilgi_ver(self): # this method was overrived
        print("Hesap türü: Toplamak")

    def hesapla(self): # same
        return float(self.sayi1 + self.sayi2)

class Cikart(Hesap):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def bilgi_ver(self): # this method was overrived
        print("Hesap türü: Çıkartmak")

    def hesapla(self): # same
        return float(self.sayi1 - self.sayi2)

class Carp(Hesap):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def bilgi_ver(self): # this method was overrived
        print("Hesap türü: Çarpmak")

    def hesapla(self): # same
        return float(self.sayi1 * self.sayi2)

class Bol(Hesap):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2)

    def bilgi_ver(self): # this method was overrived
        print("Hesap türü: Bölmek")

    def hesapla(self): # same
        if self.sayi2 == 0:
            return f"Hata: Payda sıfır olamaz"
        else:
            return float(self.sayi1 / self.sayi2)
