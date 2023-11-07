from array import *

my_array = array("i", [10, 20, 20, 20, 30, 40, 50])

# using append in array insert an element at last index of array
print("Before append = ", my_array)
my_array.append(60)
print("After Append = ", my_array)


# using insert we can insert any element at any index by mentioning the index number insert(index,element)
print("Before insert", my_array)
my_array.insert(1, 70)
print("After insert", my_array)

# Using remove we can remove any element that present in array if it is not present than it gives error
print("Before Remove", my_array)
my_array.remove(30)
print("After Remove", my_array)

# pop removes an element from last index of array it does not take any arguments
print("before pop = ", my_array)
my_array.pop()
print("after pop", my_array)

# index return the index number of element that passes as argument in index function
print("the index number of 40 is  = ", my_array.index(40))

# tolist is used to convert to transform an array into list
my_list = [my_array.tolist()]
print("the copied list from array is = ", my_list)

# the count returns how many time the element appears in array which passesd as argument in array
print("the 20 repeated in array " , my_array.count(20), " time ")
