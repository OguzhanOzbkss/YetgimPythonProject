#Kullanıcıdan yemek fiyatı bahşiş ve kaç kişi oldukları alınacak kişi başı fiyat gösterilecek

food_money = int (input("Lütfen Yemek Ücretini Giriniz : "))
tip_money = int (input("Lütfen Bahşiş Ücretini Giriniz : "))
person = int (input("Lütfen Kişi Sayısı Giriniz : "))

result = ((food_money*person)+ tip_money)/person

print("Kisi bası düşen para =", result)