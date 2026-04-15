liste = ["adam", "Berke", 343, "23" , 43, "sdnf", 23, 56, 65, "adaö", 3, 34, 21, 213, 2323, "Nber"]
string_list = [item.upper() for item in liste if isinstance(item, str)]
print(string_list)