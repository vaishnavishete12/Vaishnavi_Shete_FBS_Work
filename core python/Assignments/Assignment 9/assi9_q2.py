#write program to Check Armstrong Number Using Recursion

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def armstrong_sum(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** power) + armstrong_sum(n // 10, power)

num = int(input("Enter a number: "))

digits = count_digits(num)
result = armstrong_sum(num, digits)

if result == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")