l = int(input("Enter Value of length(in cms):"))
if l>0:
    inch = float((l*l)/2.54)
    print("length is inches",inch)
else:
    print("invalid entry")