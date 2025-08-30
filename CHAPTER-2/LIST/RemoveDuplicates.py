# QUESTION 7 :- Remove Duplicates from a list Without Using set().

l = list(map(int,input("Enter elements of list: ").split()))
unique = []

for i in (l):
    if i not in unique:
        unique.append(i)

print("List :",unique)