#bubble sort in python

from array import *

my_array = array('i',[])
count = int(input("Enter Total Counts For Elements : "))
for i in range(count):
   element = int(input("Enter Value of Element : "))
   my_array.append(element)
print("You have Entered elements like : ",my_array)

def bubblesort(arr):
   totalcount = len(arr)
   for i in range(count):
      for j in range(totalcount - i -1):
         if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
bubblesort(my_array)
print("Sorted Array is = ",my_array)