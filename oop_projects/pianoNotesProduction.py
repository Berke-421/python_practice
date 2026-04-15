import random
class Piano:

    __sheet_music = ["do-","re","mi","fa","sol","la","si","do", "re", "mi", "fa", "sol", "la", "si", "do+"]
    @property
    def sheed_music(self): return self.__sheet_music

    def __production(self, meas, amount):
        __notes = []
        i = 1
        amount *= meas
        while i <= amount:
            choose = random.randint(0, len(self.__sheet_music) - 1)
            note = self.__sheet_music[choose]
            __notes.append(note)
            if i % meas == 0: __notes.append("|")
            i += 1
        return __notes

    def four_measures(self, amount):
        if amount <= 0 or not isinstance(amount, int): raise ValueError ("The amount was not entered correctly.")
        else: return self.__production(4, amount)

    def three_measures(self, amount):
        if amount <= 0 or not isinstance(amount, int): raise ValueError ("The amount was not entered correctly.")
        else: return self.__production(3, amount)


berke = Piano()
a = berke.four_measures(3)
print(a)

