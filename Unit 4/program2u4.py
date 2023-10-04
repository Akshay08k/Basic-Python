list = ['a',0]

for val in list:
    try:
        print("Division By Zero : ",val/val)
    except ZeroDivisionError:
        print("Zero DIvision Error cant be divided by zero")
    except TypeError:
        print("TypeError")
