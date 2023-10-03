x = {}
print("How Many Elements You Want : ")
n = int(input())
for i in range(n):
    print("Enter Key Roll No : ")
    k = input()
    print("Enter its Value Marks : ")
    v = int(input())
    x.update({k:v})

print("The Dictionary Is : ",x)