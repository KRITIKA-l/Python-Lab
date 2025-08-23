# PROGRAM 9 :- Write a Python program to find the sum of digits of a number.

num = int(input("Enter a number :"))
sum = 0
temp = num
while temp > 0:
    sum += temp % 10
    temp //= 10

print(f"Sum of Digits of {num} is {sum}.")