# Aufgabe 3

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(9))


def next_prime(n):
    num = n * 2 ** 2
    numlst = [x for x in range(1, num)]

    numlst = numlst[n:]

    for i in numlst:
        if is_prime(i) == True:
            return i


print(next_prime(8))
