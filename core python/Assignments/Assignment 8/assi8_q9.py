#Check Whether the Entered Number is a Palindrome or Not (Using Function).

def palindrome(num):
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    if rev == num:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if palindrome(n):
    print(n, "is a Palindrome Number")
else:
    print(n, "is Not a Palindrome Number")