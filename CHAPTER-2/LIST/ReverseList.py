# QUESTION 5 :- Reverse a list without using reverse() function or slicing [::-1].

list = input("Enter elemensts of list: ").split()

for i in range(len(list)//2):
    list[i], list[-i-1] = list[-i-1], list[i]
    
print("Reversed List :",list)   