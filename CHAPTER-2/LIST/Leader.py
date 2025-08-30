# QUESTION 12 :- Find Leaders in a list (element is leader if it is greater than all elements to its right).

l = list(map(int,input("Enter elements :").split()))
n = len(l)

leaders=[]
rightmax = l[-1]
leaders.append(rightmax)

for i in range(n-2,-1,-1):
    if l[i] > rightmax:
        rightmax = l[i]
        leaders.append(rightmax)

leaders.reverse()
print("Leaders : ",leaders)