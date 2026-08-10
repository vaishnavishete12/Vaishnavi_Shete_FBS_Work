#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + …..n!

n = int(input("Enter n: "))
fact = 1
sum = 0

for i in range(1, n + 1):
    fact *= i
    sum += fact

print("Sum =", sum)
#b) N + N² + N³ + ... + Nᴺ
N = int(input("Enter N: "))
sum = 0

for i in range(1, N + 1):
    sum = sum + (N ** i)

print("Sum =", sum)
#c) Geometric series (1 + 2 + 4 + 8 + ... n terms)
n = int(input("Enter number of terms: "))
term = 1
sum = 0

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)
#d) S = a + a²/2 + a³/3 + ... + a¹⁰/10
a = int(input("Enter value of a: "))
sum = 0

for i in range(1, 11):
    sum = sum + (a ** i) / i

print("Sum =", sum)
#e) S = x − x²/3 + x³/5 − x⁴/7 + ... up to n terms
x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))
sum = 0

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)
    if i % 2 == 0:
        sum = sum - term
    else:
        sum = sum + term

print("Sum =", sum)





