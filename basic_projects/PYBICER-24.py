import time

print("isim matik")

depo = []


print("İsim girişi başladı bitirmek için '0' tuşuna basın")
time.sleep(3) # 3 saniye bekler

while True:
    isim = input("İsim = ")

    if isim == '0': break

    if any(a.isdigit() for a in isim):
        print("Sayı tespit edildi")
        continue

    depo.append(isim)

print("Alfabetik sıralama")
depo.sort(reverse=True)
print(depo)
