# WAP to calculate total salary of an employee

basic = int(input("Enter Basic Salary: "))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra

print("Basic Salary =", basic)
print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)