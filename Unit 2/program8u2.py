def modify(lst):
    lst.append(9)
    print(lst,id(lst))

lst = [1,2,3,4]
modify(lst)
print(lst,id(lst))