#write the program to calculate the Power of a Number Using Recursion.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)

print("Result =", result)