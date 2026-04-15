import random
from person_profile import MaleNames, FemaleNames, TurkishSurname, PersonalityTrait, Profession

class NpcNameGenerator:
    __oneOrDoubleName = None
    __maleOrFemale = None
    __name = ""; __secondname = "" ; __job = ""; __age = 0; __personality = ""

    __npc_dict = {}
    @property
    def npc_dict(self): return self.__npc_dict

    def createNpc(self, amount):
        i = 0
        while i <= amount:
            self.__oneOrDoubleName = random.randint(0,1) # çift veya tek isim gelme ihtimali
            self.__maleOrFemale = random.randint(0, 1) # erkek veya kız isim gelme ihtimali
            self.__job = str(random.choice(list(Profession)).name) # iş sınıfından alıp stringe çevirip atama
            self.__personality = str(random.choice(list(PersonalityTrait)).name) # özellik sınıfından alıp stringe çevirip atama
            self.__age = random.randint(24, 65) # rastgele yaş seçip atar

            if self.__maleOrFemale == 0: # erkek gelirse
                if self.__oneOrDoubleName == 0: # tek isim gelirse
                    self.__name = str(random.choice(list(MaleNames)).name) + " " + str(random.choice(list(TurkishSurname)).name)
                    self.__npc_dict[self.__name] = {
                        "job": self.__job,
                        "age": self.__age,
                        "trait": self.__personality
                    }

                else:
                    while True: # çift isim gelirse
                        self.__name = str(random.choice(list(MaleNames)).name)
                        self.__secondname = str(random.choice(list(MaleNames)).name)
                        if not self.__name == self.__secondname:
                            self.__name = self.__name + self.__secondname + " " + str(random.choice(list(TurkishSurname)).name)
                            break
                        else: continue

                    self.__npc_dict[self.__name] = {
                        "job": self.__job,
                        "age": self.__age,
                        "trait": self.__personality
                    }

            else: # kadın gelirse
                if self.__oneOrDoubleName == 0:
                    self.__name = str(random.choice(list(FemaleNames)).name) + " " + str(random.choice(list(TurkishSurname)).name)
                    self.__npc_dict[self.__name] = {
                        "job": self.__job,
                        "age": self.__age,
                        "trait": self.__personality
                    }

                else:
                    while True:
                        self.__name = str(random.choice(list(FemaleNames)).name)
                        self.__secondname = str(random.choice(list(FemaleNames)).name)
                        if not self.__name == self.__secondname:
                            self.__name = self.__name + " " + self.__secondname + " " + str(random.choice(list(TurkishSurname)).name)
                            break
                        else: continue

                    self.__npc_dict[self.__name] = {
                        "job": self.__job,
                        "age": self.__age,
                        "trait": self.__personality
                    }
            i += 1

    def get_info(self):
        for namee, info in self.__npc_dict.items():
            print("-" * 35)
            print(namee)
            print(info)
            print("-" * 35)

berke = NpcNameGenerator()
berke.createNpc(30)
berke.get_info()