class Kelimematik: # Kelimematik adında bir sınıf tanımlanır
    _puan = 20 # protected nesne değişkeni, kelimenin puanını tutar
    _sonuc = None # protected nesne değişkeni, kelimenin sonucunu tutar
    __yedek = None # private nesne değişkeni, kelimenin yedeğini tutar

    def __init__(self, kelime = ""): # constructor, kelime parametresi alır ve bu parametreyi nesne değişkeni olarak atar
        self.kelime = kelime # public nesne değişkeni, kelimeyi tutar
        self.__yedek = self.kelime  # private nesne değişkeni, kelimenin yedeğini tutar, constructor içinde atama yapılır

    def uzunluk(self): # public metot, kelimenin uzunluğunu hesaplar
        self.kelime = self.kelime.replace(" ", "") # replace ile kelimedeki boşluklar kaldırılır
        return len(self.kelime) # kelimenin uzunluğu hesaplanır ve döndürülür

    def tanit(self): # public metot, kelimeyi tanıtır ve puanını hesaplar
        self._sonuc = len(self.kelime) * self._puan # kelimenin uzunluğu ile puan çarpılarak sonuc hesaplanır
        print(f"Girilen kelime: {self.__yedek}") # girilen kelimeyi ekrana yazdırır
        print(f"Puan: {self._sonuc}") # kelimenin puanını ekrana yazdırır

berke = Kelimematik("Naber dostum nasılsın") # parametre girildi
print(berke.uzunluk()) # kelimenin uzunluğunu ekrana yazdırır
berke.tanit() # kelimeyi tanıtır ve puanını ekrana yazdırır