# PROGRAM 5 :- Write a Python program that:
# a.	Takes a message as input.
# b.	Counts the number of vowels (a, e, i, o, u — both uppercase and lowercase).
# c.	Prints the vowel count.

msg = input("Enter a message : ").lower()
vowels = "aeiou"
count = 0

for ch in msg:
    if ch in vowels:
        count += 1
        
print("Vowels Count :",count)