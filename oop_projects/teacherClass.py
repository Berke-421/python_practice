class Teacher:
    tecrubelik = 5 # tecrübe adında sınıf değişkeni

    def __init__(self, ad, yas): # constructor, ad ve yas parametrelerini alır
        self.ad = ad; self.yas = yas # ad ve yas alır bu satır
        self.puan = 1 # puan atar

    def tanit(self): # public metot, öğretmeni tanıtır
        print(f"Merhaba ben öğretmen {self.ad}, ve {self.yas} yaşındayım")

    def puan(self): # public metot, öğretmenin puanını hesaplar
        self.puan += self.tecrubelik
        self.tecrubelik += 10
        return self.puan
    