# QUESTION 17 :- Create a list of marks of 5 students and find: Maximum marks, Minimum marks, Total marks, Average marks.

marks = [int(input(f"Enter marks of student {i+1}: ")) for i in range(5)]

print("Maximum marks:", max(marks))

print("Minimum marks:", min(marks))

print("Total marks:", sum(marks))

print("Average marks:", sum(marks)/len(marks))
