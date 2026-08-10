#Area ana permeter of the  given figer.

import math

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

# Area of rectangle
area_rectangle = length * breadth

# Area of semicircle
area_semicircle = (math.pi * radius * radius) / 2

# Total area
total_area = area_rectangle + area_semicircle

# Perimeter
perimeter = (2 * length) + breadth + (math.pi * radius)

print("Area of figure =", total_area)
print("Perimeter of figure =", perimeter)