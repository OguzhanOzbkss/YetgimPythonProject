#Kullanıcıdan vize final notu alınacak notları hesaplanıp harf notuyla birlikte ekrana yazılacak.

vize_not = int(input("Lütfen vize notunuzu giriniz : "))
vize_not = vize_not*0.4
final_not = int(input("Lütfen Final Notunuzu Giriniz : "))
final_not =final_not*0.6
if final_not<50:
     print("Direk FF Aldınız")
result = vize_not+final_not

if result > 0 and result <= 49 :
        print(f"Notunuz {result} Harf Notunuz 'FF' ")
elif result <=54:
    print(f"Notunuz {result} Harf Notunuz 'DD' ")
elif result <=59:
    print(f"Notunuz {result} Harf Notunuz 'DC' ")
elif result <=65:
    print(f"Notunuz {result} Harf Notunuz 'CC' ")
elif result <=72:
    print(f"Notunuz {result} Harf Notunuz 'CB' ")
elif result <=79:
    print(f"Notunuz {result} Harf Notunuz 'BB' ")    
elif result <=87:
    print(f"Notunuz {result} Harf Notunuz 'BA' ")
elif result <=100:
    print(f"Notunuz {result} Harf Notunuz 'AA' ")                    