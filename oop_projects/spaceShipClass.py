from difflib import Match

class Uzaygemisi: # uzay gemisi sınıfı tanımlanır
    uydu = 3 # sınıf değişkeni

    def __init__(self, ad, crew): # constructor, ad ve crew parametrelerini alır
        self.ad = ad
        self.crew = crew
        self.can = 100

    def tanit(self): # public metot, uzay gemisini tanıtır
        print(f"{self.ad} uzay gemisi ve {self.crew} adet mürettebatı sizi selamlar")
        print(f"Can: {self.can}")

    def darbeal(self): # public metot, uzay gemisi darbe alırsa canı azalır
        self.can -= 10
        return self.can

    def tamir(self): # public metot, uzay gemisi tamir edilir ve canı artar
        self.can += 10
        if self.can >= 100:
            self.can = 100
        return self.can

class Gezegengemi(Uzaygemisi): # uzaygemisi sınıfından kalıtım alır, türev sınıf
    def __init__(self, ad, crew, nufus):
        super().__init__(ad, crew)
        self.nufus = nufus

    def tanit(self): # public metot, gezegengemisi tanıtır
        print(f"Merhaba yolcu! ")
        super().tanit() # super() ile ana sınıftaki metot işlemi çağrılır
        print(f"Bu gemide {self.nufus} kişi yaşıyor")
