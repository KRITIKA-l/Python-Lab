# QUESTION 4 :- Reverse a list without using reverse() function or slicing [::-1].

nums = input("Enter elemensts of list: ").split()

for i in range(len(nums)//2):
    nums[i], nums[-i-1] = nums[-i-1], nums[i]
print("Reversed List :",nums)   