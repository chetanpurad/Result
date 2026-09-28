name = input("Enter student name: ")

mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent:", name)
print("Total:", total)
print("Average:", average)

if mark1>= 35 and mark2>=35 and mark3>=35:
    print("Result: PASS")
else:
    print("Result: FAIL")

if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 40:
    print("Grade: C")
else:
    print("Grade: D")
