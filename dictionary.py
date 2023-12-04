#key -value şeklinde çalışır

sehirler=["kocaeli","istanbul"]
plakalar=[41,34]

# print(plakalar[sehirler.index("kocaeli")])

# plakalar={"kocaeli":41,"istanbul":34}
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"]=6
# plakalar["kocaeli"]="new value"  #içindeki bir değere yeni bir value değeri atanabilir
# print(plakalar)

users={
    "umutyildiz":{
        "roles":["admin","user"],
        "age":18,
        "email":"umut@gmail.com",
        "address":"eskişehir"
    },
    "alier":{
        "age":36,
        "email":"alier@gmail.com",
        "address":"eskişehir"
    }
}
print(users["umutyildiz"]["roles"])
print(users["alier"]["age"])