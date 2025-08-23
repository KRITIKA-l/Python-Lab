# PROGRAM 13 :- Write a Python program to demonstrate an infinite loop with a break condition.

while True:
    n = int(input("Enter a number :"))
    if n == 0:
        print("Loop Stopped !")
        break
    print("You entered :",n)
