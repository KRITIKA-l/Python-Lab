# PROGRAM 3 :- Write a Python program to display the first and last colors from the list.

num = int(input("Enter Number of elements in list : "))
list = []
for i in range(num):
    element = input(f"Enter element {i+1} :")
    list.append(element)

print(f"First Element of the list is {list[0]}.")
print(f"Last Element of the list is {list[-1]}.")