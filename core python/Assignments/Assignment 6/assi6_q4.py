rows = 5

for i in range(rows):
    ch = 65      # ASCII value of 'A'
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()