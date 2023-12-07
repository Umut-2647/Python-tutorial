numbers=[1,2,3,4,5]

for num in numbers:
    print(num)

names=["Umut","Burak","Sedat","Dilek"]

for name in names:
    print(f"My name is {name}")

name2="Umut Yildiz"
for n in name2:
    print(n)

tuple=[(1,2),(3,5),(5,7),(7,9)]
for a,b in tuple:
    print(a,b)


d={"k1":1,"k2":2,"k3":3}
"""for item in d.items():
    print(item)"""   #key value degerleri birlikte gelir
for key,value in d.items():
    print(key,value)  #key value degerleri parantez dışında ayrı ayrı gelir

