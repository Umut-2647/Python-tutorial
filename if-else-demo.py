import datetime


# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 
"""
isim=input("İsminizi girin :")
yas=int(input("Yasinizi girin :"))
egitim=input("Egitim bilgilerinizi girin :")

if(yas>=18):
    if(egitim.lower()=="lise" or egitim.lower()=="üniversite"):
        print(f"{isim} Ehliyet alabilirsin")
    else:
        print(f"{isim} Ehliyet alamazsin egitim durumun yetersiz")
else:
    print(f"{isim} Ehliyet alamazsin yasin tutmuyor")
"""

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24   0
# 25-44  1
# 45-54  2
# 55-69  3
# 70-84  4
# 85-100 5

"""yazili1=float(input("1. yazili notunuzu giriniz :"))
yazili2=float(input("2. yazili notunuzu giriniz :"))
sozlu=float(input("Sozlu notunuzu giriniz :"))
ortalama=(yazili1+yazili2+sozlu)/3

if(ortalama>=0) and (ortalama<=24):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 0") 
elif(ortalama>=25) and (ortalama<=44):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 1")
elif(ortalama>=45) and (ortalama<=54):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 2")
elif(ortalama>=55) and (ortalama<=69):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 3") 
elif(ortalama>=70) and (ortalama<=84):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 4")
elif(ortalama>=85) and (ortalama<=100):
    print(f"Ortalamaniz {ortalama} ve not bilgisi 5")
else:
    print("Yanlis bilgi girdiniz")"""





# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

"""tarih=input("Araciniz hangi tarihte trafige cikti?(yyyy/aa/gg) :")
tarih=tarih.split("/")
trafigeCikis=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigeCikis
days=fark.days

print(days)
if(days<=365):
    print("1.servis araligi")
elif(days>365) and (days<=365*2):
    print("2. servis araligi")
elif(days>366*2) and (days<=365*3):
    print("3. servis araligi")
else:
    print("Hatali servis")"""
