class student:
    def __init__(self):
        self.name = "Akshay"
        self.age = 20
        self.marks = 140

    def display(self):
        print("Name Of The Student = ",self.name)
        print("Age Of The Student = ",self.age)
        print("Marks Of The Student = ",self.marks)

s = student()
s.display()