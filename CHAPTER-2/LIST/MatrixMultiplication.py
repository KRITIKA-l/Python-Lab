# QUESTION 16 :- Write a program to multiply two matrices using lists.

r1 = int(input("Enter number of rows for Matrix 1: "))
c1 = int(input("Enter number of columns for Matrix 1: "))
r2 = int(input("Enter number of rows for Matrix 2: "))
c2 = int(input("Enter number of columns for Matrix 2: "))

if c1 != r2:
    print("Matrix multiplication not possible (columns of Matrix 1 must equal rows of Matrix 2).")
else:
    print("Enter elements of Matrix 1 :")
    A = []
    for i in range(r1):
        row = list(map(int, input().split()))
        if len(row) != c1:
            print(f"Please enter exactly {c1} numbers")
            row = list(map(int, input().split()))
        A.append(row)

    print("Enter elements of Matrix 2:")
    B = []
    for i in range(r2):
        row = list(map(int, input().split()))
        if len(row) != c2:
            print(f"Please enter exactly {c2} numbers")
            row = list(map(int, input().split()))
        B.append(row)

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]


    print("Resultant Matrix:")
    for row in result:
        print(row)
