# QUESTION 19 :- Write a program to zip two lists (names & scores) and print name → score pairs.

names = input("Enter names separated : ").split()
scores = list(map(int, input("Enter scores separated : ").split()))

for name, score in zip(names, scores):
    print(f"{name} : {score}")