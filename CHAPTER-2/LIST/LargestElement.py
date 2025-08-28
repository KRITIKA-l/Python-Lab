# QUESTION 2 :- Write a program to input 5 numbers in a list and print the largest one.

num = []
for i in range(5):
    n = int(input(f"Enter element {i+1} : "))
    num.append(n)

largest = num[0]
for i in range(5):
    if (num[i]>largest):
        largest = num[i]

print(f"Largest number in {num} is {largest}.")