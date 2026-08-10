rows = 4

for i in range(rows):
    # Print leading spaces
    for j in range(rows - i - 1):
        print(" ", end=" ")

    # Print numbers
    for j in range(i + 1):
        if j == 0 or j == i:
            print(1, end=" ")
        else:
            print(i, end=" ")
    print()