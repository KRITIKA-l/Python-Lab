# QUESTION 11 :- Flatten a Nested List.

n = int(input("Enter number of sublist : "))
nested = []
flatten = []

for i in range(n):
    sublist = list(map(int,input(f"Enter elements for sublist {i+1} :").split()))
    nested.append(sublist)

for i in nested:
    for j in i:
        flatten.append(j)

print("Flattened List : ",flatten)
