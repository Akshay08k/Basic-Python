#nested tuple information

emp  = ((10,"Ajay,4000"),(20,"Vijay",1000),(30,"Sanjay",12000))
print(sorted(emp))
print(sorted(emp,reverse=True))
print(sorted(emp,key=lambda x:x[1]))
print(sorted(emp,key=lambda x:x[1]))
