rows = 5

for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # Print stars
    for j in range(2 * i + 1):
        print("*", end=" ")

    print()