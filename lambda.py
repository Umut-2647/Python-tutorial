# def square(num):
#     return num**2


square=lambda num:num**2

numbers=[1,3,5,9,12,10,6,48,4]

"""result=list(map(lambda num:num**2,numbers)) 
result=list(map(square,numbers)) 
result=square(14)
for item in map(square,numbers):
    print(item)"""

#mapın görevi dizideki tüm elemanları fonksiyona göndermek
#map kullanıldığı zaman ya list üzerinden ya da for dongüsüyle içindeki elemanlara ulaşmamız gerekir

def check(num): return num%2==0
# result=list(filter(check,numbers))
result=list(filter(lambda num: num%2==0,numbers))

print(result)




