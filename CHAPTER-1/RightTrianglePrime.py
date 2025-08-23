# PROGRAM 12 :- Write a Python program using nested loops to print a right triangle pattern of prime numbers.

row = int(input("Enter number of rows : "))
num = 2

for i in range(1, row+1):
    for j in range(i):
        while True:
            count = 0
            for k in range(1, num+1):
                if num % k == 0:
                    count += 1
            if count == 2:
                print(num, end=" ")
                num += 1
                break
            else:
                num += 1
    print()