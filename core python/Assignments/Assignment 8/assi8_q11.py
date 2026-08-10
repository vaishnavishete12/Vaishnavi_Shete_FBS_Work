#Check Whether a Number is an Armstrong Number or Not (Using Separate Functions).

def count_digits(num):
    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp = temp // 10

    return count


def is_armstrong(num):
    digits = count_digits(num)
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** digits)
        temp = temp // 10

    if total == num:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_armstrong(n):
    print(n, "is an Armstrong Number")
else:
    print(n, "is Not an Armstrong Number")