x = [10,20,30,40]
y = [100,120,130,140]
print("Combined List : ",x+y)

print("Repeat X :",x*2)
m = x
print(" m = ",m)

lst = x[:]
print("x = ",x)
print("Cloned list = ",lst)

x[1] = 99
print("x = ",x)
print("lst = ",lst)