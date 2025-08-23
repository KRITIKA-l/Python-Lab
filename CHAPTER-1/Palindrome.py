# PROGRAM 20 :- Write a Python program to check if a string is a palindrome.

string = input("Enter a string :")
rev = ""

for ch in string:
    rev = ch + rev

if rev == string:
    print("String is Palindrome")
else:
    print("String is Not Palindrome.")