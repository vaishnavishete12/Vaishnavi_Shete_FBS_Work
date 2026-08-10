rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if i == 1 or j == 1 or i + j == rows + 1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()