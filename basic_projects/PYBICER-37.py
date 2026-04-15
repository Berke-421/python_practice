print("Berke Biçer")

mtn1 = input("Birinci metni giriniz = ")
sy1 = len(mtn1)

mtn2 = input("İkinci metni giriniz = ")
sy2 = len(mtn2)

if sy1 > sy2:
    print(f"\'{mtn1}\' metni \'{mtn2}\' metninden daha uzun")
elif sy2 > sy1:
    print(f"\'{mtn2}\' metni \'{mtn1}\' metninden daha uzun")
else:
    print(f"iki metin eşit uzunlukla")
