UmutHesap={
    "ad":"Umut",
    "hesapNo":"123546879",
    "bakiye":3000,
    "ekHesap":2000
}

AliHesap={
    "ad":"Ali",
    "hesapNo":"78956231",
    "bakiye":2000,
    "ekHesap":1000
}


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if(hesap["bakiye"]>=miktar):
        hesap["bakiye"]-=miktar
        print("paranizi cekebilirsiniz")
        BakiyeSorgula(UmutHesap)
    else :
        toplam=hesap["bakiye"]+hesap["ekHesap"]
        if (toplam>=miktar):

            ekHesapKullanim=input("Ek hesap kullanilsin mi (e/h) :")

            if(ekHesapKullanim=="e"):
                ekHesapKullanilacakMiktar=miktar-hesap["bakiye"]
                hesap["bakiye"]=0
                hesap["ekHesap"]-=ekHesapKullanilacakMiktar
                print("paranizi cekebilirsiniz")
                BakiyeSorgula(UmutHesap)
            else :
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bakiye bulunmaktadir")
        else :
            print("Üzgünüz paranizi cekemezsiniz")
            BakiyeSorgula(UmutHesap)


def BakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir,Ek hesap limitiniz ise {hesap['ekHesap']} TL dir.")

paraCek(UmutHesap,3000)

print("****************")

paraCek(UmutHesap,2000)
