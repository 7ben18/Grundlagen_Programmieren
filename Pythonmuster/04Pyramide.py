def pyramide(n):
    for x in range(1, n+1):
        print(" " * (n - x) + "#" * (2 * x - 1) + " " * (n - x))

pyramide(6)

