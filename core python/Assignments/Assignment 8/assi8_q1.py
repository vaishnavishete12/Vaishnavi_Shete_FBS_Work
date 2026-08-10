def area_rectangle(length, width):
    area = length * width
    return area

length = float(input("Enter length: "))
width = float(input("Enter width: "))

result = area_rectangle(length, width)

print("Area of Rectangle =", result)