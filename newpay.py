# Yeni Fiyat Hesaplama Fiyat ve indirim oranı alınacak

pay = int(input("Lütfen Fiyat giriniz : "))
discount = int(input("Lütfen İndirim Tutarını Giriniz : "))

result = pay * (discount/100)
print(f"İndirimli Fiyat : {pay-result}")   