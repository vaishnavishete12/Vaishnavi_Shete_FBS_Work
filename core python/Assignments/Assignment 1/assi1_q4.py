# Write a program to enter P,T,R and calculate simple Intrest
P = int (input("Enter Principal Amount(P): "))
T = int (input("Enter Time (T): "))
R = int (input("Enter Rate of Intrest (R): "))

SI = (P * T * R) / 100
print("Simple Intrest =", SI)