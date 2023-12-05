x=6
hak=5
devam="e"
# result= (5<x<10)

# and
# or
# not

result=(x>5) and (x<10)
result=(hak>0) and (devam=="e")

# x 5 ve 10 arasında bir çift sayı mı?

result=((x>5 and x<10)) and (x%2==0)


print(result)