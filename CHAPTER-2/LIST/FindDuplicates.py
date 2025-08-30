# QUESTION 10 :- Find All Duplicates in a list.

l = list(map(int,input("Enter elements of list: ").split()))
checked = []

for i in range(len(l)):
    if l[i] not in checked:   
        positions = [i]        
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                positions.append(j)
        if len(positions) > 1:   
            print(f"Element {l[i]} is duplicate at positions {positions}")
        checked.append(l[i]) 