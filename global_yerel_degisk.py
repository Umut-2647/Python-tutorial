#global scope
x="Global scope"

def funciton():
    x="Local scope"   #asıl x değişkenini değiştirmez
    print(x)

funciton()
print(x)

###########################

#global
name="Umut"

def changeName(new_name):
    name=new_name
    print(name)

changeName("Berk")
print(name)


###########################

name="Global string"


def greeting():
    # name="Berk"

    def Hello():
        # name="Ada"
        print("Hello "+name)
    Hello()

greeting()

###########################

"""x=50
def text(x):
    print(f"x :{x}")   #fonsiyon içinde yapilan değişiklikler global değişkeni etkilemez
    x=100
    print(f"changed x to {x}")

text(x)
print(x)"""


x=50
def text():
    global x   #global yazıldığı zaman global değişkende değiştirilmiş olur
    print(f"x :{x}")   
    x=100
    print(f"changed x to {x}")

text()
print(x)

