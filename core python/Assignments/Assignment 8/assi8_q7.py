#Write a program to find the Sum of Digits of a Number.

def sum_of_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total

n = int(input("Enter a number: "))

result = sum_of_digits(n)

print("Sum of digits =", result)