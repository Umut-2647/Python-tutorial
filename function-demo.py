# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

"""def yazdir(kelime,adet):
        print(kelime*adet)

yazdir("Umut\n",5)"""

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

"""def listeCevir(*parametres):
    liste=[]
    for param in parametres:
        liste.append(param)
    return liste

result=listeCevir(5,4,6,8,"Merhaba","Umut")
print(result)"""

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

"""def asalSayiBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi>1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break
            else:
                print(sayi)

sayi1=int(input("sayi 1 :"))
sayi2=int(input("sayi 2 :"))

asalSayiBul(sayi1,sayi2)"""


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

"""def tamBolen(sayi):
    liste=[]
    for i in range(1,sayi+1):
        if(sayi%i==0):
            liste.append(i)
    return liste



sayi=int(input("Sayi gir :"))
result=tamBolen(sayi)
print(result)"""

        

