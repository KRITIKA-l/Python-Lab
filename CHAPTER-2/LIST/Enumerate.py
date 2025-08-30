# QUESTION 22 :- Use enumerate() on a list of fruits and print index with fruit name.

fruits = input("Enter fruits : ").split()

for index, fruit in enumerate(fruits):
    print(index + 1, fruit)