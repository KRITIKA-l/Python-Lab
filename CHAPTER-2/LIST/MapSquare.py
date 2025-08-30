# QUESTION 20 :- Write a program using map() to square every element of a list.

numbers = list(map(int, input("Enter numbers: ").split()))
squared = [x**2 for x in numbers]
print("Squared:", squared)