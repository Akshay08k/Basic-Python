class Father:
    property = 400000
    def __init__(self, property):
        self.property = property

    def display_property(self):
        print("Father's property ", self.property)


class Son(Father):
    def __init__(self, property):
        super().__init__(property)
        self.property1 = property

    def display_property(self):
        print("Total property of child : ", self.property1 + Father.property)


s = Son(25000)

s.display_property()


# without using super() method

print("\nWithout using super() method")


class Father1:
    def __init__(self):
        self.property = 80000

    def display_property1(self):
        print("Father's property : ", self.property)


class Son1(Father1):
    pass


s = Son1()

s.display_property1()
