# 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
#        dictionary içinde saklayınız.

#     2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
"""ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yilmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }"""

ogrenciler={}
number=input("Numarayi girin :")
name=input("Ad girin :")
surname=input("Soyad girin :")
phone=input("Telefon numarasini girin :")

# ogrenciler[number]={
#     "ad":name,
#     "soyad":surname,
#     "telefon":phone
# }


ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number=input("Numarayi girin :")
name=input("Ad girin :")
surname=input("Soyad girin :")
phone=input("Telefon numarasini girin :")

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

number=input("Numarayi girin :")
name=input("Ad girin :")
surname=input("Soyad girin :")
phone=input("Telefon numarasini girin :")

ogrenciler.update({
    number:{
        "ad":name,
        "soyad":surname,
        "telefon":phone
    }
})

print("*"*50)


val=input("Ogrenci numarasini girin :")
ogrenci=ogrenciler[val]
print(ogrenci)
print(f"Aradiğiniz {val} nolu ogrencinin adi: {ogrenci["ad"]} soyadi: {ogrenci["soyad"]} telefon numarasi: {ogrenci["telefon"]}")
