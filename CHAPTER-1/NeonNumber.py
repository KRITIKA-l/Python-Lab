# PROGRAM 7 :- Write a program to check whether a number it is neon number.
 
num = int(input("Enter a number :"))
square = num**2
sum = 0

while square > 0:
    sum = square % 10
    square //= 10

if sum == num:
    print(f"{num} is a Neon number.")
else:
    print(f"{num} is not a Neon number.")