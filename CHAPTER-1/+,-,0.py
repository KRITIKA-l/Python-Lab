# PROGRAM 16 :- Write a Python program to read a number and check if it is positive, negative, or zero using nested if-else.

num = int(input("Enter a number :"))

if num >= 0:
    if num == 0:
        print("Number is Zero.")
    else:
        print("Number is Positive.")
else:
    print("Number is Negative.")