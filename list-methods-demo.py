names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]



# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")

# 2-  "Sena" değerini listenin başina ekleyiniz.
names.insert(0,"Sena")
names.insert(len(names),"Mehmet")

# 3-  "Deniz" ismini listeden siliniz.
#names.remove("Deniz")
# 4-  "Deniz" isminin indeksi nedir ?
val=names.index("Deniz")
# 5-  "Ali" listenin bir elemanı mıdır ?
val="Ali" in names
# 6-  Liste elemanlarını ters çevirin.
names.reverse()
years.reverse()
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
stri="Chevrolet,Dacia"
ad=stri.split(",")
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
result=min(years)
val=max(years)
# 11- years dizisinde kaç tane 1998 değeri vardır ?
result=years.count(1998)
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar=[]

marka=input("Marka :")
markalar.append(marka)
marka=input("Marka :")
markalar.append(marka)
marka=input("Marka :")
markalar.append(marka)

print(markalar)
# print(ad)
# print(result)
# print(val)
# print(years)
# print(names)


