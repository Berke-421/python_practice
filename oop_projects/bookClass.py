
"""
Kitaplık: Kitap sınıfı oluştur (isim, yazar, sayfa sayısı).
 __str__ metodunu kullanarak kitabı yazdırdığında güzel bir özet dönmesini sağla.
"""

class Book:
    __varmi = False
    __sonuc = []
    __bittimi = False
    __bit = ""

    def __init__(self, isim, yazar, sayfa):
        if not isim.isdigit():
            self.isim = isim
        else: self.isim = "Unkown"

        self.__varmi = any(char.isdigit() for char in yazar)
        if self.__varmi:
            __sonuc = [char for char in yazar if not char.isdigit()]
            self.yazar = "".join(__sonuc)

        try:
            self.sayfa = int(sayfa)
            if self.sayfa > 100000: raise ValueError
        except ValueError:
            self.sayfa = "Sayfa belirtilmedi"

    def bilgiver(self, goster=True):
        self.__bit = "okunmadı" if self.__bittimi else "okuldu"
        if goster:
            print(f"Kitap: {self.isim}, yazar: {self.yazar}, sayfa: {self.sayfa}, durum: {self.__bit}")
        else:
            return f"Kitap: {self.isim}, yazar: {self.yazar}, sayfa: {self.sayfa}, durum: {self.__bit}"

    def oku(self):
        return "Okumaya başlandı"

class Roman(Book):
    def __init__(self, isim, yazar, sayfa):
        super().__init__(isim, yazar, sayfa)

class Tarih(Book):
    def __init__(self, isim, yazar, sayfa):
        super().__init__(isim, yazar, sayfa)



