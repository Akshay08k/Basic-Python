class student:
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def set_marks(self,marks):
        self.marks = marks
    def get_marks(self):
        return self.marks
    
count = int(input("Please Enter Total Count Of Student : "))

for i in range(count):
    s = student()
    name = input("Enter the name : ")
    s.set_name(name)
    marks = int(input("Enter the marks : "))
    s.set_marks(marks)

    print("Hii",s.get_name())
    print("Your Marks = ",s.get_marks())