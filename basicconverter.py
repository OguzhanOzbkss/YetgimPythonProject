# 1 metres = 3.2808398950131 Feet
# 1 kilograms = 2.2046226218488 pounds

kilogram_or_metres = input("Metre Dönüştürmek için 'M' Kilogram Dönüştürmek için 'K'ya basınız :")

kilogram_or_metres=kilogram_or_metres.lower()

if kilogram_or_metres == "k" : 
    kg_value = int (input("Lütfen kilo giriniz : "))
    result = kg_value * 2.2046226218488
    print(f"Pound Değeriniz {result}")
elif kilogram_or_metres == "m":
    mt_value = int(input("Lütfen metre giriniz : "))
    result = mt_value * 3.2808398950131
    print(f"Feet Değeriniz {result}")
else :
    print("Farklı seçim yaptınız Tekrar deneyiniz !!")