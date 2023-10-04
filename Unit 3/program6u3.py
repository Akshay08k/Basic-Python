class demo:
    count = 0

    def __init__(self):
        demo.count += 1
    @staticmethod
    def count_object():
        print("Total Number instace Created = ",demo.count)
    
obj1 = demo()
obj2 = demo()
obj3 = demo()
obj4 = demo()
obj5 = demo()
demo.count_object() 