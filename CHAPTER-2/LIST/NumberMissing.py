# QUESTIONS 13:- Find the Missing Number from 1 to n.

n = int(input("Enter n : "))
nums = list(map(int,input("Enter elements :").split()))

missing=[]

for i in range(1,n+1):
    if i not in nums:
        missing.append(i)

print("Missing Numbers : ", missing)