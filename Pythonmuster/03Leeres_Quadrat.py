def leeres_quadrat(n):
    for x in range(n):
        if x == 0 or x == n - 1:
            print("#" * n)
        else:
            print("#" + (n - 2) * " " + "#")


for a in range(1,5 + 1):
    leeres_quadrat(a)