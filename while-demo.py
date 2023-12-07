sayilar = [1,3,5,7,9,12,19,21]
# 1: sayilar listesini while ile ekrana yazdırın.
"""i=0
while(i<len(sayilar)):
    print(sayilar[i])
    i+=1"""




#2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
"""baslangic=int(input("Baslangic degerini girin :"))
bitis=int(input("Bitis degerini girin :"))

while baslangic<=bitis:
    if(baslangic%2==1):
        print("Girilen araliktaki tek sayilar :",baslangic)
    baslangic+=1"""




# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""x=100
while(x<=100 and x>=1):
    print(x)
    x-=1"""




# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
"""numbers=[]
sayac=1
while sayac<=5:
    sayi=int(input("Bİr sayi girin :"))
    numbers.append(sayi)
    sayac+=1
numbers.sort()
print(numbers)"""

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler=[]
adet=int(input("Kac adet urun eklemek istiyorsunuz? :"))
i=1
while(i<=adet):
    name=input("Urun isimini giriniz :")
    price=int(input("Urun fiyatini giriniz :"))
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1
for urun in urunler:
    print(f"Urun adi :{urun['name']} Urun fiyati :{urun['price']}")
# eger dışarıda çift tırnak kullanılıyorsa içerde tek tırnak kullanılmalıdır.
