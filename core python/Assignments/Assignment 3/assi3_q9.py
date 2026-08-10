# Program to input 5 subject marks and display grade

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 35:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")