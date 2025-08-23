# PROGRAM 22 :- Write a Python program to convert a string to Title Case without using built-in functions.

string = input("Enter a string :")

result = ""
upper = True

for ch in string:
    if ch == "":
        result += ch
        upper = True
    elif upper:
        result += ch.upper()
        upper = False
    else:
        result += ch.lower()

print("Title Case : ",result)