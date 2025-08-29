# QUESTION 7 :- Remove Duplicates from a list Without Using set().

list = list(map(int,input("Enter elements of list: ").split()))
unique = []

for i in (list):
    if i not in unique:
        unique.append(i)

print("List :",unique)