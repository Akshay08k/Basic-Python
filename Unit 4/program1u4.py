x = float(input("Enter 1st Number : "))
y = float(input("Enter 2st Number : "))

try:
    print("Division  : ",x/y)
except ZeroDivisionError:
    print("Cant Division By Zero")
finally:
    print("This Will Always Print")
