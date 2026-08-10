rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print("  ", end="")

    # Print numbers
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()