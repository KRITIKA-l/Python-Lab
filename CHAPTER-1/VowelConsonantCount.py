# PROGRAM 19 :- Write a Python program to count vowels and consonants in a string.

string = input("Enter string :").lower()
vowels = "aeiou"
vowel = 0
consonant = 0

for ch in string:
    if ch.isalpha():
        if ch in vowels:
            vowel += 1
        else:
            consonant += 1

print("Vowels :",vowel)
print("Consonant :",consonant)
