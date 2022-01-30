def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n

def prime_dist(start, dist):
    n = start
    start1 = next_prime(start)
    start2 = next_prime(start1)
    while start2 - start1 != dist:
        if start2 > n * 10:
            return None
        else:
            start2 = next_prime(start2)
            start1 = next_prime(start1)

    return (start1, start2)


print(prime_dist(3,6))
print(prime_dist(1021,10))

# Geil es klappt