import random
import string

sayac = 0
liste = []

while sayac < 4:
    length = random.randint(10, 31)

    match sayac:
        case 0:
            for _ in range(length):
                liste.append(random.randint(0, 101))

        case 1:
            for _ in range(length):
                rastgele_str = "".join(random.choices(string.ascii_letters, k=5))
                liste.append(rastgele_str)

        case 2:
            for _ in range(length):
                x = round(random.uniform(0, 101), 5)
                liste.append(x)

    sayac += 1

print("Eleman sayısı: ", len(liste))
print("int veri tipi sayısı: ", len([x for x in liste if isinstance(x, int)])  )
print("float veri tipi sayısı: ", len([x for x in liste if isinstance(x, float)])  )
print("string veri tipi sayısı: ", len([x for x in liste if isinstance(x, str)])  )
print(liste)