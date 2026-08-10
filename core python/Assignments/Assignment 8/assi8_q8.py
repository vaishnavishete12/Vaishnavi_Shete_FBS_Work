#find Reverse of a Number (Using Function).

def reverse_number(num):
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev

n = int(input("Enter a number: "))

result = reverse_number(n)

print("Reverse of the number =", result)