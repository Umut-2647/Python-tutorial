#range()

"""for item in range(2,10):   #2 dan başlar ve 9 a kadar gider(10 dahil degil)
      print(item)

for item in range(50,100,2):   #50 den başlar ve 100 a kadar gider ve 2 arttırır(100 dahil degil)
      print(item)

print(list(range(50,100,2)))  #liste seklinde yazdirir"""


#enumerate
"""index=0
greeting="Hello there"
for letter in greeting:
    print(f"İndex : {index} Letter : {letter}")
    index+=1"""

""""greeting="Hello there"
for letter in enumerate(greeting):
    print(letter)"""

"""greeting="Hello there"
for index,letter in enumerate(greeting):
    print(f"İndex : {index} Letter : {letter}")"""


#zip

list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))   #listeleri index numarasina gore birebir birlestirir

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):  #elemanlar tek tek gelir
    print(a,b,c)