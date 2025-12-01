#random 3 sayı üretilecek ve bu 3 sayıya karşılık gelen nesneler ile oynanıcak.
# 1=Tas 2= kagıt 3=makas
import random

print("Hadi Taş Kağıt Makas Oynayalım!!!")

user_skor = 0 
comp_skor = 0

while user_skor < 3 and comp_skor < 3 :
    user = int(input("1 = Taş , 2 = Kağıt, 3 = Makas !! Seçim Yap !! : "))
    comp = random.randint(1,3)
    print(comp)
    if user == comp :
        print("Berabere")
    elif user == 1 and comp == 2:
         print("Comp Win +1")
         comp_skor = comp_skor+1
    elif user == 2 and comp == 3:
         print("Comp Win +1")
         comp_skor = comp_skor+1
    elif user == 3 and comp == 2:
         print("User Win +1")
         user_skor = user_skor+1
    elif user == 3 and comp == 1:
         print("Comp Win +1")
         comp_skor = comp_skor+1
    elif user == 2 and comp == 1:
         print("User Win +1")
         user_skor = user_skor+1
    elif user == 1 and comp == 3:
         print("Comp Win +1")
         user_skor = user_skor+1
    else :
         print("Hata Var")
       
if user_skor > comp_skor :
     print("User Won")
else :
     print("Comp Won")
