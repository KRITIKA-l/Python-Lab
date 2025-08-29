# QUESTION 3 :- Write a function that takes a list and returns a new list with only even numbers.

n = int(input("Enter number of element :"))
list = []

for i in range(n):
    name = int(input(f"Enter element {i+1} : "))
    list.append(name)

even = [i for i in list if i % 2 == 0]
print("NEW LIST : ",even)