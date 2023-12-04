fruits={"apple","banana","orange"}
# print(fruits[0])  #indekslenemez
for x in fruits:
    print(x)
fruits.add("cherry")
fruits.update(["mango","grape","apple"])
fruits.remove("mango")
fruits.discard("banana")
fruits.pop()  #rastgele bir veriyi siler
print(fruits)

# myList=[1,2,4,4,5,1,2]
# print(set(myList))  #tekrarlanan elemanlar listeden çıkartılır
