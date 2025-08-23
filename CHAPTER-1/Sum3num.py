# PROGRAM 4:- Write a Python program to calculate the sum of three given numbers. If the values are equal, return thrice their sum.

a = int(input("Enter first number :"))
b = int(input("Enter Second number :"))
c = int(input("Enter third number :"))

sum = a+b+c
if (a==b==c):
    print("Values are equal, 3*Sum : ",3*sum)
else :
    print("Sum :",sum)
