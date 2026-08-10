#WAP to print Armstrong number within a given range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if num == total:
        print(num)