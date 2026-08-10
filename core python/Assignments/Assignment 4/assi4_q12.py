#Write a program to check if given number is Armstrong number or not.
#(Hint : 153 = 111 + 555 + 333 , 1634 = 1111 + 6666 + 333*3 +
#444*4)

num = int(input("Enter a number: "))
temp = num
count = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")