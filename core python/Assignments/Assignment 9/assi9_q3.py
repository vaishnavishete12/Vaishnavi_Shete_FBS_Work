#write program to Reverse a Given Number Using Recursion.

def reverse_num(n, rev):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))
result = reverse_num(num, 0)

print("Reverse number =", result)