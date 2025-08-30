# QUESTION 21 :- Write a program using filter() to extract only even numbers from a list.

numbers = list(map(int, input("Enter numbers: ").split()))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)