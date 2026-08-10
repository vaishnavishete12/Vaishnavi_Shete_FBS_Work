# Program to check whether a triangle is valid or not using angles

a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a + b + c == 180:
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")