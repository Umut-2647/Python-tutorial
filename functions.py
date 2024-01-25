"""def sayHello():
    print("Hello")"""

"""def sayHello(name="user"):
    print("Hello "+name)

sayHello("Umut")
sayHello()"""  #parametre gönderilmediği zaman varsayılan olarak user bilgisi aktarılıyor

def sayHello(name="user"):
    return "Hello "+name


msg=sayHello("Umut")
print(msg)

def total(num1,num2):
    return num1+num2

result=total(10,20) #return dediğimiz için bir değişkene aktardık

print(result)

def yasHesapla(dogumYili):
    return 2023-dogumYili

ageUmut=yasHesapla(2005)
ageAli=yasHesapla(2014)
ageBerk=yasHesapla(1989)

print(ageUmut,ageAli,ageBerk)


def emekliligeKacYilKaldi(dogumYili,name):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi


    """
    yas=yasHesapla(dogumYili)
    emeklilik=65-yas

    if(emeklilik>0):
        print(f"Sayin {name} emekliliğinize {emeklilik} yil kaldi")
    else:
        print("Zaten emeklisiniz")
    
emekliligeKacYilKaldi(2005,"Umut")

print(help(emekliligeKacYilKaldi))

print(help(list.append))
