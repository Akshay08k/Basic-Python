class MyClass:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print("Sum of three numbers : ", a + b + c)

        elif a != None and b != None:
            print("Sum of two numbers : ", a + b)

        else:
            print("Enter two or three arguments ")


m = MyClass()

m.sum(10, 20, 30)

m.sum(10.5, 20.55)

m.sum(200)
