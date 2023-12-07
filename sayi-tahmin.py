import random

rastgele=int(random.random()*100) # veya rastgele=random.randint(1,100)
print(rastgele)
sayac=0
can=int(input("Kac caniniz olsun :"))
hak=can

while(hak>0):
    hak-=1
    sayac+=1
    tahmin=int(input("Tahmin giriniz :"))
    if(rastgele>tahmin):
        print("daha buyuk bir sayi giriniz")
    elif(rastgele<tahmin):
        print("daha kucuk bir sayi giriniz")
    else :
        print(f"Tebrikler sayiyi {sayac}.denemede buldunuz,Puaniniz {(100)-((100/can))*(sayac-1)}")
        break
    if(hak==0):
        print(f"Hakkiniz doldu... Sayi {rastgele} ydi")
