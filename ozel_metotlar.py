mylist=[1,2,3,4]
#myString="hello there"

# print(len(mylist))
# print(len(myString))


class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print("movie objesi olusturuldu")


    def __str__(self):
        return f"{self.title} by {self.director}"
    
    def __len__(self):
        return self.duration

    def __del__(self):
        print("Film objesi silindi")

m=Movie("film adi","film yonetmeni",120)


"""print(mylist)   #liste oldugu icin direkt liste calisir"""
print(m)        #def str calisir
"""print(len(m))   #def len calisir


print(m)        #def del calisir"""

