rows = 5

# Upper half
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower half
for i in range(rows - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()