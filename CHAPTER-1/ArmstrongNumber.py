# PROGRAM 8 :- Write a Python program to check if a number is an Armstrong Number.

num = int(input("Enter a number :"))
temp = num
count, sum = 0, 0

while temp > 0:
    count += 1
    temp //= 10

temp = num

while temp > 0:
    sum += (temp % 10) ** count
    temp //= 10

if num == sum:
    print(f"{num} is a armstrong number.")
else:
    print(f"{num} is not a armstrong number.")