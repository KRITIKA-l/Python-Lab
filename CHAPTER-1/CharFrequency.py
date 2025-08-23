# PROGRAM 21 :- Write a Python program to find the frequency of each character in a string.

string = input("Enter a string :")
counted = ""

for char in string:
    if char not in counted:
        freq = 0
        for c in string :
            if c == char:
                freq += 1
        print(f"{char} : {freq}")
        counted += char