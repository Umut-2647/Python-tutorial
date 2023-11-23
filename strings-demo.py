website="http://www.sadikturan.com"
course="Python kursu: Baştan sona python programlama Rehberiniz"

#1- 'course' karakter dizisindeki kaç tane karakter bulunmaktadır

lenght=len(course)
result =len(website)
print(lenght)

# 2-'website' içinden www karakterlerini alın
print(website[7:10])

# 3-'website' içinden com karakterlerini alın
print(website[22:25])
print(website[result-3:result])

# 4-'course' içinden ilk 15 ve son 15 karakterlerini alın
print(course[:15]) #ilk 15
print(course[-15:])

# 5-'course' ifadesindeki karakterleri tersten yazın
print(course[::]) #bütün karakterleri al
print(course[::-1]) #tersten yaz

s="12345"*5 # 5 tane 12345 yazar
print(s[::5])


name,surname,age,job="Umut","Yildiz",18,"Mühendis"
print(f"Benim adim {name} {surname}, Yaşim {age} ve mesleğim {job}")

# Hello world ifadesindeki w harfini 'W' ile değiştirin
deg="Hello world"
deg=deg[0:6] +'W'+deg[-4:]
deg.replace("w","W")
print(deg)

# abc ifadesini yan yana 3 defa yazınız

print("abc"*3)

