# PROGRAM 6 :- Write a program to calculate sum of odd number upto n.

num = int(input("Enter a limit : "))
sum = 0
i = 1
while i<=num:
    if i%2!=0:
        sum += i
    i += 1 
print(f"Sum of {num} odd numbers is {sum}.")