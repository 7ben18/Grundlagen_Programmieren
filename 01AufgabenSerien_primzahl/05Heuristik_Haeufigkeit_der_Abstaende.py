def eratosthenes(n):
    zahlenliste = []
    primezahlen = []
    for z in range(2,n,1):
        zahlenliste.append(z)

    for i in range(2,n,1):
        if i in zahlenliste:
            primezahlen.append(i)
            zahlenliste.remove(i)
        for a in zahlenliste:
            if a % i == 0:
                zahlenliste.remove(a)
    return primezahlen

def distances(primes):
    distance = []
    for x in range(0,len(primes)-1,1):
        diff = (primes[x+1] - primes[x])
        #diff = abs(diff)
        distance.append(diff)
    return distance

print(distances(eratosthenes(100)))


def heuristic(n):
    liste = n
    haeufigkeit = []
    num0 = 0
    for x in n:
        if x == 0:
            num0 += 1
    num0_x = (0, num0)
    haeufigkeit.append(num0_x)
    num1 = 0
    for x in n:
        if x == 1:
            num1 += 1
    num1_x = (1, num1)
    haeufigkeit.append(num1_x)
    return haeufigkeit


print(heuristic(distances(eratosthenes(100))))
print(heuristic(distances(eratosthenes(50))))
