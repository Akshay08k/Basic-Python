max = lambda x,y : x if x>y else y
a,b = [int(n) for n in input("Enter two no :").split(' ')] #give a space at the time of enteriing values
print("Bigger No :",max(a,b)) 