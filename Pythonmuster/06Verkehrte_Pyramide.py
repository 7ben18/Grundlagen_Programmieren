def verkehrte_pyramide(n:int) -> str:
    for x in range(n,0,-1):
        print(" " * abs(x - n) + "#" * (2 * x - 1) + " " * abs(x - n))


for num in range(5):
    verkehrte_pyramide(num)
