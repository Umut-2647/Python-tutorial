#Kalıtım=>Miras alma

#Person=> name,lastname,age,eat(),run(),drink()
#Student(Person) , Teacher(Person)

class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        print("Person created")

    def who_am_i(self):
        print("I am person")


class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("Student created")
    def who_am_i(self):
        print("I am a student")


p1=Person("Umut","Yildiz")
s1=Student("Ali","Er",363)

print(p1.firstname+" "+p1.lastname)
print(s1.firstname+" "+s1.lastname+" "+str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()