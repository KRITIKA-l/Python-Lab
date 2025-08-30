# QUESTION 23 :- Use reversed() function to reverse a list without slicing.

l = list(map(int, input("Enter numbers: ").split()))
rev = list(reversed(l))
print("Reversed list:", rev)