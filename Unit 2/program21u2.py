x = {}

print("How Many Players? : ")
n = int(input())
for i in range(n):
    print("Enter " , i+1 , " Player Name : ")
    k = input()
    print("Enter Runs : ")
    v = int(input())
    x.update({k:v})

print(x)
print("Enter Players name : ")
name = input()
runs = x.get(name,-1)
if(runs == -1):
    print("Player Not Found")
else:
    print("{} made runs {}".format(name,runs))