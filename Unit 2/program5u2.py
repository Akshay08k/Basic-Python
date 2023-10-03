from array import *

my_array = array('i',[10,20,30,40,50])

print(my_array)

search = int(input("Enter the Element to search it's index : "))

index = my_array.index(search)

print("the index of element is  = ",index)