class student:
    def __init__(self,name,age,city="ahmedabad"):
        self.name = name
        self.age = age
        self.city = city
    def display(self):
        print("Name = ",self.name)
        print("age = ",self.age)
        print("city = ",self.city)

s1 = student("Akshay",20)
s1.display()
print("-----------------------")
s2 = student("Nandini",10,"London")
s2.display()
