def area_circle(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter radius: "))

result = area_circle(radius)

print("Area of Circle =", result)