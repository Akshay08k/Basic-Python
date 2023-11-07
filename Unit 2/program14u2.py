list1 = [range(10)]

for i in list1:
    print(i)

print()
list1.append(30)
print(list1)
list1[1] = 99
print(list1)
del list1[0]
print(list1)
