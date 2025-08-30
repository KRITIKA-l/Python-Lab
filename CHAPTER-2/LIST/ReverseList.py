# QUESTION 5 :- Reverse a list without using reverse() function or slicing [::-1].

l = input("Enter elemensts of list: ").split()

for i in range(len(l)//2):
    l[i], l[-i-1] = l[-i-1], l[i]
    
print("Reversed List :",l)   