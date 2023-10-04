class student:
    def __init__(self,name="Akshay",age=23,marks=100):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Marks : ",self.marks)
        
s = student("Akshay",20,100)
s.display()