demet = ()

while True:
    girdi = input("Gir = ")

    if girdi == "x":
        print("İşlem bitti")
        break

    demet += (girdi,)

print("En uzun girdi: ", max(demet))
print("En kısa girdi: ", min(demet))