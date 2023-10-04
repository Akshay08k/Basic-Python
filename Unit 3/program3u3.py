class demo:
    var = 100
    @classmethod
    def new_modify(cls):
        cls.var +=1
s1 = demo()
s2 = demo()

print("value of var in obj1 = ",s1.var)
print("value of var in obj2 = ",s2.var)

print("Modify value of var in ob1")
s1.new_modify()
print("value of var in obj1 = ",s1.var)
print("value of var in obj2 = ",s2.var)


