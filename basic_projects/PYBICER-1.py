from time import sleep

berke = 123
print("berke veri tipi: ", type(berke))

print("berke sayısı string diline çeviriliyor...")

sleep(3)

berke = str(berke) # str() metodu nesneyi string'e çevirir
print("berke değişkeni başarıyla string veri tipine dönüştürüldü")

print()

print("berke veri tipi: ", type(berke))