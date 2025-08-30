# QUESTION 6 :- Find the Second Largest Element in a list.

l = list(map(int,input("Enter elements of list: ").split()))

largest = slargest = float('-inf')

for i in range(len(list)):
    if l[i] > largest:
        slargest = largest
        largest = l[i]
    elif l[i] > slargest and l[i] != largest:
        second = l[i]

if slargest == float('-inf'):
    print("No second largest element (all elements may be same).")
else:
    print("Second Largest:", slargest)
