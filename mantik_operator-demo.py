# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
""" sayi=int(input("Sayi :"))
result=sayi>0 and sayi<100
print(f"Girdiginiz sayi {sayi} ve 0-100 arasinda olma durumu {result}")
"""
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
sayi=int(input("Sayi :"))
result=sayi>0 and sayi%2==0
print(f"Girdiginiz sayi {sayi} ve pozitif cift olma durumu {result}")
"""

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 

"""email="email@umtyildiz.com"
password="54456"

girilenEmail=input("Email :")
girillenPassword=input("Parola :")

result=(girilenEmail==email)  and  (girillenPassword==password)
print(f"Kullanici girisi :{result}")
"""

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''sayi1=int(input("1.sayiyi girin :"))
sayi2=int(input("2.sayiyi girin :"))
sayi3=int(input("3.sayiyi girin :"))

result= (sayi1>sayi2) and (sayi1>sayi3)
print(f"1.sayi en buyuktur {result}")

result= (sayi2>sayi1) and (sayi2>sayi3)
print(f"2.sayi en buyuktur {result}")


result= (sayi3>sayi2) and (sayi3>sayi1)
print(f"3.sayi en buyuktur {result}")
'''
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a) ortalama 50 üstünde bile ise final en az 50 olmalıdır
# b) finalden 70 alındığında ortalamanın önemi olmasın

"""vize1=int(input("1. vize notunu girin :"))
vize2=int(input("2. vize notunu girin :"))
final=int(input("Final notunu girin :"))
ortalama=((vize1+vize2/2)*0.6) + (final*0.4)


result=(ortalama>=50)
print(f"Ogrencinin ortalamasi {ortalama} ve gecme durumu {result}")


result=(ortalama>=50) and (final>=50)
result=(ortalama>=50) or(final>=70)

print(f"Ogrencinin ortalamasi {ortalama} ve gecme durumu {result}")
"""




# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.

ad=input("Adinizi girin :")
kilo=float(input("Kilonuzu girin :"))
boy=float(input("Boyunuzu girin :"))

indeks=(kilo)/(boy**2)

zayif=(indeks>=0) and (indeks<=18.4)
normal=(indeks>18.4) and (indeks<=24.9)
fazlak=(indeks>24.9) and (indeks<=29.9)
obez=(indeks>29.9 ) and (indeks<=34.9)

print(f"{ad} kilo indeksin : {indeks} ve kilo değerlendirmen zayif: {zayif}")
print(f"{ad} kilo indeksin : {indeks} ve kilo değerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin : {indeks} ve kilo değerlendirmen fazla kilolu: {fazlak}")
print(f"{ad} kilo indeksin : {indeks} ve kilo değerlendirmen obez: {obez}")


#     Formül =  kilo/boy kare
# 0-18.4     =>   Kilolu
# 18.5-24.9  =>   Normal
# 25.0-29.9  =>   Fazla kilolu
# 30.0-34.9  =>   Obez
