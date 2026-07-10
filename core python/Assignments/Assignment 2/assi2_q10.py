#Write a program to reverse three-digit number

num = int(input("Enter a three-digit number: "))

# Reverse the number
reverse = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

# Display the reversed number
print("Reversed number:", reverse)