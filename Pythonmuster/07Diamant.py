def diamant(n):
    for x in range(1, n + 1):
        print(" " * (n - x) + "#" * (2 * x - 1) + " " * (n - x))
    for q in range(n - 1, 0, -1):
        print(" " * abs(q - n) + "#" * (2 * q - 1) + " " * abs(q - n))


for num in range(10):
    diamant(num)
