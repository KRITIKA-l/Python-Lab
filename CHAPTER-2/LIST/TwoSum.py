# QUESTION 8 :- Pair elements that sum to a given value (Two-Sum Problem).

l = list(map(int,input("Enter elements of list: ").split()))
target = int(input("Enter a target number : "))

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            print("Pair: ", l[i], l[j])