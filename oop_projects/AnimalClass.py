class Animals: # hayvan sınıfını tanımladık
    is_alive = True # sınıf değişkeni, tüm hayvanların canlı olduğunu tutar
    def __init__(self, name, money): # constrcutor
        self.name = name # nesne değişkeni
        self.money = money

    def sleep(self): # bütün hayvanlar için ortak bir metot yazdık
        print(f"{self.name} is sleeping") # varsayılan işlem


class Cat(Animals):
    def chas(self): # cat sınıfına ait bir metot yazdık
        print(f"{self.name} is chasing")

class Mouse(Animals):
    pass

class Rabbit(Animals):
    def sleep(self): # ana sınıftaki metot override edilerek kendi davranışını yazdık
        print(f"{self.name} fell into a restless rabbit sleep.")

class Bird(Animals):
    def sleep(self): # override edildi
        print(f"{self.name} is sleeping with angrily") 

cat = Cat("Tom", 34)
mouse = Mouse("jerry", 23)
rabbit = Rabbit("Bugs Buny", 89)
bird = Bird("boncuk", 2)

print("-" * 30)

print(cat.name, cat.money, cat.is_alive)
cat.sleep()
cat.chas()

print("-" * 30)

print(mouse.name)
mouse.sleep()

print("-" * 30)

print(rabbit.name, rabbit.money)
rabbit.sleep()

print("-" * 30)

print(bird.name, bird.money, bird.is_alive)
bird.sleep()

print("-" * 30)
