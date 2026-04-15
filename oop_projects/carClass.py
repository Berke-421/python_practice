class Araba:
    _tekerlek_sayisi = 4 # protected nesne değişkeni

    def __init__(self, marka, model): # constructor
        self.marka = marka # public nesne değişkeni markayı tutar
        self.model = model # public nesne değişkeni modeli tutar

    def bilgigoster(self): # public nesne metodu, arabaya ait bilgileri ekrana yazdırır
        print(f"Benim arabam {self.marka}, {self.model} modeldir.") # f-string kullanarak ekrana yazdırma işlemi yapıldı


berke = Araba("Opel", 2004) # Araba sınıfından bir nesne oluşturuldu, marka "Opel" ve model 2004 olarak belirlendi
berke.bilgigoster() # oluşturulan nesnenin bilgigoster metodunu çağırarak arabaya ait bilgileri ekrana yazdırır

bicer = Araba("Togg", 2023) # Araba sınıfından bir nesne oluşturuldu, marka "Togg" ve model 2023 olarak belirlendi
bicer.bilgigoster() # oluşturulan nesnenin bilgigoster metodunu çağırarak arabaya ait bilgileri ekrana yazdırır