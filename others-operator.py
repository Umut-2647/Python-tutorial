# Identity Operator: is
"""
x = y= [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is z)  # x ile z farkli bir referansa sahip olduğu için false değeri döner
"""

x=[1,2,3]
y=[2,4]

del x[2]
y[1]=1
y.reverse()

print(x==y)
print(x is y)
print(x is not y)

# Membership Operator: in
x=["banana","apple"]
print("banana"in x)

name="Umut"
print("u"in name)