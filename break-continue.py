"""name="Umut Yildiz"

for n in name:
    if(n=="u"):
        continue
    print(n)"""

#1-100 e kadar tek sayilarin toplami
toplam=0
x=0
while x<=100:
    x+=1
    if(x%2==0):
        continue
    toplam+=x
print(toplam)