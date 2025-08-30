# QUESTION 9 :- Rotate a list by k positions.

l = list(map(int,input("Enter elements of list: ").split())) 
k = int(input("Enter number of positions to rotate: "))

k = k % len(l)  

print("Rotated List (Left): ", l[k:] + l[:k])
print("Rotated List (Right): ", l[-k: ] + l[:-k])
