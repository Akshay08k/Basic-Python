list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

for item in list1:
    if item in list2:
        print(item,"common")



for item in list1:
    if item not in list2:
        print(item,"are not common")
        print(list1[item],"not common")
