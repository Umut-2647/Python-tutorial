# class

class Person:
    #class attributes
    address="no information"

    #constructor(yapıcı metot)
    def __init__(self,name,year):

        self.name=name
        self.year=year
        print("Init metodu calisti")

    #methods
    def intro(self):
        print("Hello "+self.name)

    def caluculateAge(self):
        return 2024-self.year




p1=Person("Umut",2005)
p1.intro()
print(p1.caluculateAge())




"""#updating
p1.name="ali"
p1.address="Eskisehir"

print(f"name :{p1.name} and year: {p1.year} and address: {p1.address}")
print(p1)"""



class Circle:
    pi=3.14

    def __init__(self,yaricap=1):
        self.yaricap=yaricap

    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
        
    def alanHesapla(self):
        return self.pi*(self.yaricap**2)
    

#c1=Circle() # deger belirtilmezse yaricap=1 olur 
    
c2=Circle(10)
print(f"c2 nin alani {c2.alanHesapla()} ve cevresi {c2.cevreHesapla()}")