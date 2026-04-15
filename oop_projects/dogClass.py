class Dog:
    def __init__(self, name):
        self.name = name
        self.genus = "Unkown"

    def bark(self):
        print("The dog barked")

    def information(self):
        print(f"Name: {self.name}")
        print(f"Genus: {self.genus}")

class Golden(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.genus = "Golden"

    # geçersiz kılındı ve kendi işlemini yazdık
    # It was overridden and we implemented our own logic
    def bark(self):
        print("The Golden dog barked")

aa = Golden("Karabaş")
aa.bark()