def is_prime4(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
print(is_prime4(17)) # True
print(is_prime4(11)) # True
print(is_prime4(9)) # False

def liste_prime_zahlen(n):
    return [x for x in range(2, n) if is_prime4(x)]
print(liste_prime_zahlen(50))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]