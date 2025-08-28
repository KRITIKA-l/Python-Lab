# QUESTION 1 :- Create a list of student names. Access the 1st, 3rd, and last name.

n = int(input("Enter number of element :"))

student = []
for i in range(n):
    name = input(f"Enter name of student {i+1} : ")
    student.append(name)

if n >= 3:
    print("1st Name:", student[0])
    print("3rd Name:", student[2])
    print("Last Name:", student[-1])
else:
    print("Not enough students to access 1st, 3rd, and last name.")