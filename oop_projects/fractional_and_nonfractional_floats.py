import random
from random import randint

class AutonumberFloat:
    number = None
    __possibility = [1,2,3]

    def __autoint(self, a=0, b=0):
        if a==0 or b==0:
            tempo = random.randint(0, 100)
            return tempo
        else:
            tempo = random.randint(a, b)
            return tempo

    def __autofloat(self,a=0,b=0):
        if a==0 or b==0:
            self.rnd = random.randint(1, 10)
            tempo = round(random.uniform(1.0, 100.0), self.rnd)
            return float(tempo)
        try:
            aa = int(a); bb = int(b)
            rnd = random.randint(1, 10)
            tempo = round(random.uniform(aa,bb), rnd)
            return tempo
        except ValueError:
            aa = self.__autoint(); bb = self.__autoint()
            self.rnd = random.randint(1,10)
            tempo = round(random.uniform(aa,bb), self.rnd)
            return float(tempo)

    def OneIntwoChance(self):
        berke = random.randint(1, 2)
        if berke == 1:
            self.number = self.__autoint()
            return float(self.number)
        else:
            self.number = self.__autofloat()
            return self.number

    def maybe_float_one_third(self,a=0,b=0): # üçte bir float çıkacak
        if a==0 or b==0:
            indx = random.randint(0, len(self.__possibility) - 1)  # 0,1,2 arasında rastgele bir sayı üretir indeks için
            if not indx == 1:  # eğer indeks 1 değilse float atar
                self.number = self.__autoint()
                return float(self.number)
            else:  # eğer 1 çıkarsa float atar
                self.number = self.__autofloat()
                return self.number
        else:
            indx = random.randint(0, len(self.__possibility) - 1)  # 0,1,2 arasında rastgele bir sayı üretir indeks için
            if not indx == 1:  # eğer indeks 1 değilse float atar
                self.number = self.__autoint(a,b)
                return float(self.number)
            else:  # eğer 1 çıkarsa float atar
                self.number = self.__autofloat(a,b)
                return self.number

    def maybe_int_one_third(self, a=0, b=0): # üçte bir int çıkacak
        if a==0 or b==0:
            indx = random.randint(0, len(self.__possibility) - 1)
            if not indx == 1:
                self.number = self.__autofloat()
                return self.number
            else:
                self.number = self.__autoint()
                return float(self.number)
        else:
            indx = random.randint(0, len(self.__possibility) - 1)
            if not indx == 1:
                self.number = self.__autofloat(a,b)
                return self.number
            else:
                self.number = self.__autoint(a,b)
                return float(self.number)
