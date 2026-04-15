class Car: # araba sınıfı tanımladık
    tekerlek = 4 # sınıf değişkeni, tüm arabaların tekerlek sayısını tutar

    def __init__(self, marka, model, yil): # constructor, marka, model ve yıl parametrelerini alır
        self.marka = marka; self.model = model; self.yil = yil # marka, model ve yıl atar

    def tanit(self):
        print(f"Merhaba benim arabam {self.marka} {self.model}")

    def modelisorarsa(self): # public metot, arabanın modelini sorarsa yanıtlar
        print(f"{self.yil} model kardeşim")

class Electric(Car): # Electric sınıfı Car sınıfından kalıtım alır, elektrikli araba sınıfı tanımlanır

    def __init__(self, model, marka, yil, batarya):
        super().__init__(model, marka, yil) # super() ile ana sınıftaki constructor çağrılır
        self.batarya = batarya # türev sınıfın kendi nesne değişkeni, batarya kapasitesini tutar

    def havaat(self): # public metot, hava atma metodu
        print(f"Arabamın {self.batarya} btw'si kalmış ben hemen şşarj edeyim anlarsın arabam elektrikli")

class Kulustur(Car): # Kulustur sınıfı Car sınıfından kalıtım alır, eski ve hasarlı araba sınıfı tanımlanır
    def __init__(self, model, marka, yil, hasar):
        super().__init__(model, marka, yil) # super() ile ana sınıftaki constructor çağrılır
        self.hasar = hasar # türev sınıfın kendi nesne değişkeni, hasar durumunu tutar

    # aşağıdaki metotlar türev sınıfın kendi metotları:
    def modelisorarsa(self): # public metot, arabanın modeli sorulursa
        print(f"{self.yil} model ama gayet işimi görüyor kardeşim")

    def utan(self): # public metot, arabanın hasar durumunu sorarsa yanıtlar
        print("Eh işte işimi görüyor yeter de artar bana zaten detaya gerek yok")


berke = Car("renault", "clio", 2020)
hasan = Electric("Tesla", "Y", 2024, 788)
huseyin = Kulustur("Tofas", "şahin", 1990, 40)

berke.tanit()
hasan.tanit()
huseyin.tanit()

hasan.havaat()
huseyin.utan()