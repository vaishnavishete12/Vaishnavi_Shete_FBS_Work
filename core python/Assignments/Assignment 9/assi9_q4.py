#write program to Find Sum of n Numbers Using Recursion.

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

n = int(input("Enter a number: "))
result = sum_n(n)

print("Sum =", result)