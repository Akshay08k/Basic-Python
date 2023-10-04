class Father:
    def Height(self):
        print("Height is 6.0ft")


class Mother:
    def Iq(self):
        print("IQ is 130")


class Child(Father, Mother):
    pass


c = Child()

print("Child inherited Qualties")


c.Height()

c.Iq()
