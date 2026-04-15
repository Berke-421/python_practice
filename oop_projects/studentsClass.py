class Students: # öğrenci sınıfı
    ortalama = None # ortalama şimdilik belli değil (sınıf değişkeni)

    def __init__(self, adlar, sube): # constructor
        self.adlar = dict(adlar) # parametreyi sözlüğe çevirip nesne değişkeni olarak atar
        self.sube = str(sube) # parametreyi stringe çevirip nesne değişkeni olarak atar

    def display_info(self):
        print(f"isimler: {self.adlar}, şuba:{self.sube}, okul: cumhuriyet okulu")

    def ortalama_al(self):
        return sum(self.adlar.values()) / len(self.adlar)

b1 = Students({"Berke":100, "Ali": 80, "Ayşe": 90, "Kenan": 56}, "12/C")
print(b1.ortalama_al())

