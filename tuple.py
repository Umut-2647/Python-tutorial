list=[1,2,3]
tuple=(1,"iki",3)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])

# print(len(list))
# print(len(tuple))


list=["Ayşe","Ali"]
tuple=("Mehmet","Damla","Damla")
names=("Demet","Emel","Burak") +tuple

list[0]="Fatma"
# tuple[0]="Cenk"  #tuple ve listenin farkı tuple'a atandıktan sonra elemanları değiştirilemez sabit kalır
print(names)
print(tuple.count("Damla"))
print(list)
print(tuple)