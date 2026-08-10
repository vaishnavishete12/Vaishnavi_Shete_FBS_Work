rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Print increasing numbers
    for j in range(i, 2 * i):
        print(j, end=" ")

    # Print decreasing numbers
    for j in range(2 * i - 2, i - 1, -1):
        print(j, end=" ")

    print()