import math
import random

class Company:
    __ceo = True

    def __init__(self, name, tip):
         for i in name:
             if i.isdigit():
                 print("Şirket adı rakam içeremez")
                 self.name = "unkownOperation"
                 break
             else:
                self.name = name
         for i in tip:
             if i.isdigit():
                 print("Şirket türü rakam içeremez")
                 self.tip = "unkownOperation"
                 break
             else:
                self.tip = tip

    def tanit(self):
        print(f"Şirket Türü: {self.tip}")
        print(f"Şirket adı: {self.name} şirketiyim")