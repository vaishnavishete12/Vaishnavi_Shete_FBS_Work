#Write Program to Find the Roots of a Quadratic Equation

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

d = (b * b - 4 * a * c) ** 0.5

root1 = (-b + d) / (2 * a)
root2 = (-b - d) / (2 * a)

print("Root 1 =", root1)
print("Root 2 =", root2)