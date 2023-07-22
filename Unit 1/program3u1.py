Elements = [10,20,0,40,15]
print("Before Modifying")
print(Elements)

x = bytearray(Elements)

x[0] = 88
x[1] = 99

print("After Modifying")

for i in x : print(i)