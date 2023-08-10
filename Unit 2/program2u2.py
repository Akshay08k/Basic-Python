from array import *

x = array('i', [10, 20, 30, 40, 50, 60, 70])
n = len(x)

# Printing the array elements
for i in range(n):
    print(x[i], end=",")
print("\nValued array")

# Replacing elements in the array slice
x[2:5] = array('i', [4, 5, 6])
print(x)

# Displaying array elements after slicing
print("\nDisplaying array elements after slicing:")
for i in x[2:6]:
    print(i, end=" ")
