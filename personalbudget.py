"""
Gelirler : Maaş , Yan gelirler, 
Gider : Faturalar, Kira , Yeme İçme , Genel Gider,

"""
personal_salary = int(input("Maaşınızı Yazınız : "))
personal_perks = int(input("Ek kazançlarınızın toplamını yazınız : "))
home_bill = int (input("Fatura toplamını yazınız : "))
home_rent = int(input("Kira tutarınızı yazınız : "))
home_cost = int(input("Ekstra giderlerinizi yazınız : "))

total_money = personal_perks+ personal_salary
total_cost = home_bill+home_cost+home_rent

print(f"Yemek İhtiyacınız İçin Kalan Tutarınız : {total_money-total_cost}")