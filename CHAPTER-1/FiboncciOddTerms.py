# PROGRAM 11 :- Write a Python program to print the Fibonacci sequence but only the odd terms.

num = int(input("Enter limit :"))
a, b = 0, 1

print("Odd Terms Of Fiboncci Series up to",num," :")
while a <= num:
    if a%2 != 0:
        print(a,end=" ")
    a, b = b, a+b
