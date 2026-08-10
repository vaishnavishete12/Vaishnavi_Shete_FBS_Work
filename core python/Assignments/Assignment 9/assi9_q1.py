#Sum of the Series

#1! + 2! + 3! + ... + n! (Using Recursion)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def sum_fact(n):
    if n == 1:
        return fact(1)
    return fact(n) + sum_fact(n - 1)

n = int(input("Enter the value of n: "))
print("Sum of series =", sum_fact(n))