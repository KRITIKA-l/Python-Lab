# PROGRAM 17 :- Write a Python program to print the multiplication table of a number using a for loop.

num = int(input("Enter a number :"))

for i in range(11):
    print(f"{num} X {i} = {i*num}")