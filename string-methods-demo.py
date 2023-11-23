website="http://www.sadikturan.com"
course="Python kursu: Baştan sona python programlama Rehberiniz"

# "   Hello world   " karakter dizisinin baş ve sonundaki boşlukları silin
result=("   Hello world   ").strip()

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

result=("www.sadikturan.com").strip("w.mco")

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result=course.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result=website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result=website.startswith("www")  
result=website.endswith("com")

# 6-  'website' içinde '.com' ifadesi var mı?
result=website.find("com")
result=website.find("com",0,10)
result=website.rfind("com") #sağ taraftan aramaya başlar

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result=course.isalpha()  #sadece alfabetik mi
result=course.isdigit() #rakam mı

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result=("Contents").center(50,"*")
result=("Contents").ljust(50,"*") #ifadeyi sola yapıştırır ve sağına 50 tane yıldız koyar 

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result=course.replace(" ","-")
result=course.replace(" ","-",5) #sadece 5 tane karakteri değiştirmiş olabilir

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result=("Hello World").replace("World","There")

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

result=course.split(" ")

print(result)