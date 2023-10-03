print("----------------------------------")
print("positional arguments : ")
print("----------------------------------")
def attach(s1,s2):
    s3 = s1 + s2
    print("Final String = " + s3)
attach("New "," York")


print("----------------------------------")
print("Keyword Arguments")
print("----------------------------------")
def grocessory(item,price):
    print("item = ",item)
    print("price = ",price)
grocessory(item = 'sugar',price=50.75)
grocessory(price=80,item='oil')

print("---------------------------------")
print("default arguments")
print("---------------------------------")
def grocessory2(item,price=40):
        print("item = ",item)
        print("price = ",price)
grocessory2(item = 'sugar',price=50.75)
grocessory2(item='sugar')

