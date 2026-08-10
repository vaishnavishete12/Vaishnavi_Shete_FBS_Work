#Sum of Factorial Series 
# (1! + 2! + 3! + ... + n!) Using Function

def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter the value of n: "))

result = sum_series(n)

print("Sum of series =", result)

#(b): Sum of Series (1! + 2! + 3! + ... + n!) Using Function


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def sum_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + factorial(i)
    return total

n = int(input("Enter the value of n: "))

result = sum_factorial_series(n)

print("Sum of factorial series =", result)

#(c): Sum of Series (1¹ + 2² + 3³ + ... + nⁿ) Using Function

def power(num):
    return num ** num

def sum_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total = total + power(i)
    return total

n = int(input("Enter the value of n: "))

result = sum_power_series(n)

print("Sum of power series =", result)





