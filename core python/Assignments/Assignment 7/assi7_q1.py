rows = 5

# Upper half
for i in range(rows):
    for j in range(rows - i):
        print(" ", end="")
    print("*", end="")
    if i != 0:
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    print()

# Lower half
for i in range(rows - 2, -1, -1):
    for j in range(rows - i):
        print(" ", end="")
    print("*", end="")
    if i != 0:
        for j in range(2 * i - 1):
            print(" ", end="")
        print("*", end="")
    print()