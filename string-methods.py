message="Hello there. My name is Umut Yildiz"

# message=message.upper() #bütün harfleri büyük yapar
# message=message.lower() #bütün harfleri küçük yapar
# message=message.title() #kelimelerin ilk harfini büyük yapar
# message=message.capitalize() #sadece ilk harf büyük kalanlar küçük
message=message.strip() #girilen ifadenin başındaki ve sonundaki boş karakterleri siler
# message=message.split() #girilen ifadenin her boşluktan sonraki kelimeleri ayırır
# message=message.split(".") #girilen ifadeyi noktalardan ayırır

# message=" ".join(message) #splitin ayırdığı ifadeyi araya boşluk koyarak birleştirir

# index=message.find("Umut") #girilen ifade de Umut değerini arar ve kelimenin ilk harfinin index numarasını döner
# isFound=message.startswith("H")  #girilen ifade H ile mi başlıyor (true-false)
# isFound=message.endswith("t")  #girilen ifade n ile mi bitiyor (true-false)

# message=message.replace("Umut","Can").replace("Yildiz","Ay").replace(" ","*") #ifadeleri degistirir

# message=message.center(50,"*") #sağa ve sola 50 karakterlik boşluk yapar ve ortaya yazar

print(message)