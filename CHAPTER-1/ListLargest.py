# PROGRAM 2 :- Write a Python program to get the largest number from a list.

num = int(input("Enter Number of elements in list : "))
list = []
for i in range(num):
    element = int(input(f"Enter element {i+1} :"))
    list.append(element)

largest = list[0]
for i in range(num):
    if (list[i]>largest):
        largest = list[i]
        
print(f"Largest number in {list} is {largest}.")