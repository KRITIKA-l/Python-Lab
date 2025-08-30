# QUESTION 15 :- Write a program to create a list and sort it in increasing order.

l = list(map(int,input("Enter elements : ").split()))

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print("Sorted List :",l)
