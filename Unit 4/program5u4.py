from datetime import date


d1, m1, y1 = [
    int(i) for i in input("enter date of birth in DD/MM/YY format:").split("/")
]

dt = date(y1, m1, d1)

print("your birth date is:", dt.strftime("%d/%m/%y"))


d = date.today()

print("Todays is:", d.strftime("%d/%m/%y"))


year_d = d.strftime("%Y")

print("current year:" + year_d)


year_dt = dt.strftime("%Y")

print("birthday's year:" + year_dt)

print("Your Age is:", int(year_d) - int(year_dt))
