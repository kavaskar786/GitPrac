for i in range(1, 4):  # Outer loop for rows
    for j in range(3, 1, -1):  # Inner loop, counting down from 3 to 2
        print("*" * j + " " * i + "*" * j)
