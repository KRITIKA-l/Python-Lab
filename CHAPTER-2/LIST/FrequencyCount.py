# QUESTION 14 :- Count Frequency of Each Element in a list.

l = list(map(int,input("Enter elements : ").split()))

freq = []

for i in range(len(l)):
    if l[i] not in freq:
        count = 0
        for j in range(len(l)):
            if l[i] == l[j]:
                count += 1
        print(f"{l[i]} occurs {count} times.")
        freq.append(l[i])
