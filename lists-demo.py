# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
araba=["Bmw","Mercedes","Opel","Mazda"]

# 2-  Liste Kaç elemanlıdır ?

result=len(araba)
# 3-  Listenin ilk ve son elemanı nedir ?
result=("Ilk eleman "+araba[0]+" Son eleman "+araba[-1])

# 4-  Mazda değerini Toyota ile değiştirin.
araba[-1]="Toyota"
result=araba

# 5-  Mercedes listenin bir elemanı mıdır ?
result="Mercedes" in araba   #in operatörü arama yapar ve sınuç olarak true ya da false döner


# 6-  Listenin -2 indeksindeki değer nedir ?

result=araba[-2]

# 7-  Listenin ilk 3 elemanını alın.

result=araba[:3]
result=araba[-2:]
# 8-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

araba[-2:]=["Toyota","Reault"]
result=araba
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result=araba+["Audi","Nissan"]
# 10- Listenin son elemanını silin.
del araba[-1]
result=araba

# 11- Liste elemanlarını tersten yazdırınız.
result=araba[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 


      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","TUran",1999,[80,80,70]]
studentC=["Ahmet","Turan",1998,[80,70,90]]



# 13- Liste elemanlarını ekrana yazdırınız.
result=studentA[0]
result=studentB[1]
result=studentC[3]

# Yİğit bilgi 9 yaşında ve not ortalaması 66,67

result=f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"

print(result)