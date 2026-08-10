#Write a program to reverse a number using recursion.

def reverse(n, rev):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
result = reverse(num, 0)

print("Reversed number =", result)