from program13u2_Emp import *

basic = float(input("Enter Basic Salary : "))
gross = basic + da(basic) + hra(basic)
print("Gross Salary : {:10.2f}".format(gross))

net  = gross - pf(basic) - itax(gross)

print("gross salary  : {:10.2f}".format(net))
