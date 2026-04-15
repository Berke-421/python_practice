from abc import abstractmethod, ABC
class Hayvan(ABC):
    _tur = "Bilinmiyor"

    def __init__(self, ad):
        self.__ad = ad
    @property
    def ad(self): return self.__ad

    def al_bilgi(self):
        print(f"""
        ad: {self.__ad}
        tür: {self._tur}
        """)

    def isim_degistir(self, yeni):
        self.__ad = yeni

    @abstractmethod
    def ses(self): pass

    @abstractmethod
    def uyu(self): pass

    @abstractmethod
    def yemek(self): pass

class Kedi(Hayvan):
    _tur = "Kedi"
    def ses(self): pass
    def uyu(self): pass
    def yemek(self): pass

class Kopek(Hayvan):
    _tur = "kopek"
    def ses(self): pass
    def uyu(self): pass
    def yemek(self): pass

berke = Kedi("Güneş")
berke.al_bilgi()
berke.isim_degistir("Roketatar")
berke.al_bilgi()