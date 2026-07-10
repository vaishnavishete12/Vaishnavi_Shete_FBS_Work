#Write a program to calculate  the perentage of student based on marks of any 5 subjects 

m1 = int (input("Enter marks of Subjects 1:  "))
m2 = int (input("Enter marks of Subjects 2:  "))
m3 = int (input("Enter marks of Subjects 3:  "))
m4 = int (input("Enter marks of Subjects 4:  "))
m5 = int (input("Enter marks of Subjects 5:  "))

total = m1 + m2 + m3 + m4 + m5
percentage = total /5


print("Total Marks =",total)
print("Percentage",percentage,"%")