# x=5
# y=10
# z=20

# x,y,z=5,10,20

# x,y=y,x
# x+=5
# y//=5    #tam kısmını yazdırır

values=1,2,3,4,5

x,y,*z=values   #başına yıldız koyduğumuz zaman dizi halinde değerleri alır
print(type(values))
print(x,y,z[0])