sayi=int(input("Sayi giriniz :"))
asalmi=True

if(sayi==1):
    print("1 sayisi asal degildir")


for i in range(2,sayi):
    if(sayi%i==0):
        asalmi=False
        break

if(asalmi):
    print("Sayi asaldir")
else:
    print("Sayi asal degildir")