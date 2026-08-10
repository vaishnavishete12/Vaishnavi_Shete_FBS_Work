#write a program to find sum of digits using recursion.

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
result = sum_of_digits(num)

print("Sum of digits =", result)