 #Program to calculate area of triangle and rectangle

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
triangle_area = 0.5 * base * height

# Area of Rectangle
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
rectangle_area = length * breadth

# Display results
print("Area of Triangle =", triangle_area)
print("Area of Rectangle =", rectangle_area)