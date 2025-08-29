# QUESTION 6 :- Find the Second Largest Element in a list.

list = list(map(int,input("Enter elements of list: ").split()))

largest = slargest = float('-inf')

for i in range(len(list)):
    if list[i] > largest:
        slargest = largest
        largest = list[i]
    elif list[i] > slargest and list[i] != largest:
        second = list[i]

if slargest == float('-inf'):
    print("No second largest element (all elements may be same).")
else:
    print("Second Largest:", slargest)
