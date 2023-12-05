# 1- Girilen 2 sayıdan hangisi büyüktür ?

"""a=int(input("Bir sayi girin :"))
b=int(input("Bİr sayi daha girin :"))

result=(a>b) 
print(f"a {a} b {b} den büyüktür : {result}")
"""


# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# eğer ortalama 50 ve 50 den büyükse geçti değilse kaldı yazsın

"""
vize1=int(input("1. vize notunu girin :"))
vize2=int(input("2. vize notunu girin :"))
final=int(input("Final notunu girin :"))

ortalama=(((vize1+vize2)/2)*0.6) + (final*0.4)
print(f"Not ortalamaniz {ortalama} ve dersten geçme durumunuz {ortalama>=50}")
"""



# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

"""sayi=int(input("Sayi :"))
tekcift= (sayi%2==0)
print(f"Saiyinin cift olma durumu {tekcift}")"""




# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

"""sayi=int(input("Sayi :"))
 pozneg=(sayi>0)
 print(f"Girilen sayi {sayi} ve pozitif olma durumu {pozneg}")"""





# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

email="email@umutyildiz.com"
password="abc123"

girilenEmaiL=input("Email :")
girilenPassword=input("Parola :")

isEmail=(girilenEmaiL.lower().strip()==email)     #strip sayesinde başa ve sona konan boşluk karakterlerini siler
isPassword=(girilenPassword.strip()==password)

print(f"Email bilgisi dogru mu {isEmail} ve parola dogru mu {isPassword}")


