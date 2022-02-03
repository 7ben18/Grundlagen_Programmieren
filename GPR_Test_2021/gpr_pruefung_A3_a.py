# Aufgabe 3

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(9))


def next_prime(n):
    num = n * 2**  2
    numlst = [x for x in range(1, num)]

    numlst = numlst[n:]

    for i in numlst:
        if is_prime(i) == True:
            return i

print("next_prime")
print(next_prime(8))
print(next_prime(11))

def next_prime2(n):
    n = n + 1
    while not is_prime(n):
        n = n + 1
    return n

print("next_prime2")
print(next_prime2(8))
print(next_prime2(11))

def next_prime3(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n

print("next_prime3")
print(next_prime3(8)) # 11
print(next_prime3(11)) # 13
