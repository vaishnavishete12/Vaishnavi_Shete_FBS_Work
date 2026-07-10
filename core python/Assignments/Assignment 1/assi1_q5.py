# Write a program to enter P,T,R and calculate Compound Intrest.

P = int (input("Enter Principal Amount: "))
T = int (input("Enter Time (in years): "))
R = int (input("Enter Rate of Intrest: "))

A = P *(1 + R / 100) ** T
CI = A - P

print("Compound Intrest =", CI)
print("Total Amount =",A)