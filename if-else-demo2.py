# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""sayi=int(input("Bir sayi girin :"))

if(sayi>0):
    if(sayi%2==0):
        print("Sayi pozitif ve cifttir")
    else :
        print("Sayi pozitif ama tektir")
else:
    print("Sayi pozitif degildir")"""


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

"""email="email@umutyildiz.com"
password="12345"
girilenEmail = input('email: ')
girilenPassword = input('password: ')

if (girilenEmail == email):
    if (girilenPassword == password): 
        print('uygulamaya giris basarili.')
    else:
        print('parolaniz yanlis')
else:
    print('email bilginiz yanlis')"""






# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

"""a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and  (a > c):
    print(f'{a} en büyük sayidir.')
elif (b > a) and (b > c):
    print(f'{b} en büyük sayidir.')
elif (c > a) and (c > b):
    print(f'{c} en büyük sayidir.')"""




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

"""vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)"""

# result = (ortalama>=50) and (final>=50)
# result = (ortalama >=50) or (final>=70)

#durum 1
"""if(ortalama>=50):
    if(final>=50):
       print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: başarili')
    else:
        print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: başarisiz final notu en az 50 olmalidir')

else:
       print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: basarisiz')"""

#durum 2
"""if(ortalama>=50):
    print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: başarili')
else:
    if(final>=70):
        print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: başarili. Final notu en az 70 oldugu icin gectiniz')
    else:
        print(f'öğrencinin ortalamasi: {ortalama} ve geçme durumu: basarisiz')"""







# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


"""name = input('adiniz: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)

if (index >= 0) and (index<=18.4):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen zayif.')
elif (index>18.4) and (index<=24.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen normal.')
elif (index>24.9) and (index<=29.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu.')
elif (index>=29.9) and (index<=45.9):
    print(f'{name} kilo indeksin: {index} ve kilo değerlendirmen obez.')
else:
    print('bilgileriniz yanliş.')"""