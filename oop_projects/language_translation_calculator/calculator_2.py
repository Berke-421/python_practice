import random
from Bagımsız.oop_projeleri.language_translation_calculator.language import texts

class Hesapla:
    __olasilik = ["a", "a", "a", "b", "b", "b", "c", "c", "c"] # olasılık listesi
    def __init__(self, a, b): # constructor, iki sayı alır

        # ayrı ayrı yakalar
        try: # hata yakalar
            self.a = float(a) # ilk sayıyı float'a çevirir
        except ValueError:
            self.__ihtimal = random.randint(0, len(self.__olasilik) - 1) # olasılık listesinden rastgele bir indeks seçer
            if self.__olasilik[self.__ihtimal] == "a": # seçilen indeks "a" ise float bir sayı atar
                self.a = round(random.uniform(1.0, 100.0), 2)
            else: # değilse int bir sayı atar
                self.a = float(random.randint(0, 100))
            print(f"a = {self.a}")

        try: 
            self.b = float(b) # ikinci sayıyı float'a çevirir
        except ValueError:
            self.__ihtimal = random.randint(0, len(self.__olasilik) - 1) 
            if self.__olasilik[self.__ihtimal] == "b": 
                self.b = round(random.uniform(1.0, 100.0), 2)
            else:
                self.b = float(random.randint(0, 100))
            print(f"b = {self.b}")

    # toplama, çıkarma, çarpma ve bölme işlemleri için metotlar:
    def topla(self):
        return self.a + self.b
    def cikar(self):
        return self.a - self.b
    def carp(self):
        return self.a * self.b
    def bol(self):
        if self.b == 0:
            return "Payda sıfıra bölünemez"
        else:
            return self.a / self.b
        
# Kullanıcıdan dil seçimi yapmasını isteyelim
lang = input("Dil seç/Select language (tr/en)").lower()
if not lang in texts: # eğer seçilen dil desteklenmiyorsa varsayılan olarak Türkçe'yi kullan
    lang = "tr"
t = texts[lang] # sözlüğün içindeki hazır dil ayarını alır ve t değişkenine atar. t bundan böyle sözlük

print(t["title"])

# menu ve kullanıcı girişi için sonsuz döngü
while True:
    say1 = input(t["first_number"]); say2 = input(t["second_number"])
    berke = Hesapla(say1, say2)

    print(t["menu"])

    print(t["choice"])
    girdi = None

    while True:
        try:
            girdi = int(input())
            break

        except ValueError:
            print(t["wrong_type"])
            continue

    match girdi:
        case 1:
            print(f"{berke.a} + {berke.b}: {berke.topla()}")
        case 2:
            print(f"{berke.a} - {berke.b}: {berke.cikar()}")
        case 3:
            print(f"{berke.a} * {berke.b}: {berke.carp()}")
        case 4:
            print(f"{berke.a} / {berke.b}: {berke.bol()}")
