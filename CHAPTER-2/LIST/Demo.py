# QUESTION 18 :- Demonstrate the use of:
# •	sorted() to arrange numbers ascending and descending
# •	any() and all() with a list of boolean values

numbers = list(map(int, input("Enter numbers : ").split()))

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original numbers:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)

bool_list = list(map(int, input("Enter boolean values (0 or 1) : ").split()))
bool_list = [bool(x) for x in bool_list]  

print("Boolean list:", bool_list)
print("any() →", any(bool_list))
print("all() →", all(bool_list))