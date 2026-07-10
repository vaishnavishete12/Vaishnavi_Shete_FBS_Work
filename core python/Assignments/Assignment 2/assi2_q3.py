#Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Total inches
total_inches = (feet * 12) + inches

# Convert inches to centimeters
centimeters = total_inches * 2.54

# Convert centimeters to meters
meters = centimeters / 100

print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)