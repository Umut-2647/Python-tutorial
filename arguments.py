"""def changeName(n):
    n="Umut"

name="Berk"

changeName(name)
print(name)

def change(n):
    n[0]="Istanbul"

sehirler=["Ankara","İzmir"]

# change(sehirler)
# print(sehirler)

n=sehirler[:]  #slicing (farklı listeler meydana getirir ve orjinal listeye dokunmaz)
n[0]="  Istanbul"

print(sehirler)
print(n)

change(sehirler[:])
print(sehirler)"""


# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d))

# print(add(10,20,30,40))


# def add(*params):  #liste kullanmak istediğimiz zaman tek yıldız koyuyoruz
#     print(type(params))
#     print(params)
#     return sum((params))

# print(add(10,20,30,40,12,32))


# def add(*params):
#     sum=0
#     for n in params:
#         sum+=n
#     return sum

# print(add(10,20,30,40,12,32))

def displayUser(**args):     #bir dictionary gelecegi icin iki yildiz konur
    print(type(args))
    for key,value in args.items():
        print("{} is {}".format(key,value))

displayUser(name ="Umut",age=18,city="Eskisehir")
displayUser(name ="Yigit",age=48,city="Izmir",phone="15616845")
displayUser(name ="Ezgi",age=1,city="Ankara",phone="4566515",email="ezgi@gmail.com")

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value1",key2="value2")
