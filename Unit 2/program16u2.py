num = [10,20,30,40,50,60,70]
print("Original List : ",num)


n= len(num)
print("No Of Elements In List : ",n)


num.append(80)
print("After Appending 80 : ",num)

num.insert(1,99)
print("After Inserting 99 At Position 1 : ",num)

num1 = num.copy()
print("Newly Created List : ",num)

num.append(50)
print("AFter appending 50: ",num)

n = num.count(50)
print("No Of Times 50 Found : ",n)

num.remove(70)
print("After Removing 70 : ",num)

num.pop()
print("After Popping Element From Num : ",num)

num.sort()
print("List After Sorting : ",num)

num.reverse()
print("List Aftrer Reversing Elements : ",num)

num.clear()
print("List After Clearing All Elements : ",num)