#Program to  input two angle from user and find third angle of the triangle.
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))

c = 180 - (a + b)

print("Third angle of the triangle is:", c)