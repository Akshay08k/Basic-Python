# Binary search in python
group1 = [1, 2, 3, 4, 5]
search = int(input("Enter Element To Search: "))
found = False  # A flag to track if the element is found

for element in group1:
    if search == element:
        print("Element found in the list:", search)
        found = True
        break

if not found:
    print("Element not found in the list")
