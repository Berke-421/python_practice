class Doctor: # Doktor sınıfı tanımlanır
    tur = "Doktor" # sınıf değişkeni, tüm doktorların türünü tutar
    __katsayi = 20 # private sınıf değişkeni, doktorun tedavi puanını etkileyen katsayıyı tutar
    puan = 1 # sınıf değişkeni, doktorun tedavi puanını tutar

    def __init__(self, ad, brans): # constructor, ad ve brans paraemetrlerini alır
        self.ad = ad # public doktrun adı
        self.brans = brans # public doktorun branşı

    def tanit(self): # public metot, doktoru tanıtır
        print(f"Merhaba ben doktor {self.ad}, {self.brans} doktoruyum")

    def tedaviet(self): # public metot, doktorun tedavi etme işlemini gerçekleştirir
        print("tedavi edildi")
        self.puan += self.__katsayi
        print("Yeni puan: ", self.puan)
