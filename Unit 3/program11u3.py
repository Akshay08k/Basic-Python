class Father:
    def __init__(self):
        self.property = 90000

    def display(self):
        print("Father's property is ", self.property)


class Son(Father):
    def __init__(self):
        self.property = 25000

    def display(self):
        print("Son's property is ", self.property)


s = Son()

s.display()
