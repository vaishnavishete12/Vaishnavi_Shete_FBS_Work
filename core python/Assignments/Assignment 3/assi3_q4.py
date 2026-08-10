# Program to check whether a triangle is valid or not using sides

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")