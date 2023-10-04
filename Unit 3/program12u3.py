class father():
    property = 100000
    @classmethod
    def display_prop(cls):
        print("fathers property is : ",cls.property)

class son(father):
    pass

class daughter(father):
    property = 500000
    @classmethod
    def rdisplay_prop(cls):
        print("Total property is : ",cls.property + father.property)

s = son()
s.display_prop()
d = daughter()
d.display_prop()
