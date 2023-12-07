numbers=[]
for x in range(10):
    numbers.append(x)
print(numbers)


numbers=[x for x in range(10)]
print(numbers)


for x in range(10):
    print(x**2)

numbers=[x**2 for x in range(10)]
print(numbers)


numbers=[x**2 for x in range(10) if x%3==0] #sadece 3 e bolunen sayilarin karesini alır
print(numbers)


Mystring="Hello"
myliste=[]

for letter in Mystring:
    myliste.append(letter)
print(myliste)

myliste=[letter for letter in Mystring]
print(myliste)

years=[1983,1999,2008,1956,1986]
ages=[2023-year for year in years]
print(ages)


result=[x if x%2==0 else "TEK" for x in range(10)]
print(result)

#burdaki ifin x den sonra gelmesinin anlamı şart sağlanırsa xi yazdırmaktır

result=[]
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)


numbers=[(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers) #burda x ve y için ayrı ayrı döngü oluşturduk

