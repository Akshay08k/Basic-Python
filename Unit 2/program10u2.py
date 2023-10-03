def adder(*args):
    sum = 0
    for n in args:
        sum = sum + n
    print("sum = ",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6 )