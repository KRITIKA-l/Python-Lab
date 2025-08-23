# PROGRAM 18 :- Write a Python program to find the sum of n natural numbers using a while loop.

num = int(input("Enter limit :"))
sum = 0
i = 1

while i <= num:
    sum += i
    i += 1
    
print(f"Sum of {num} natural number is {sum}.")