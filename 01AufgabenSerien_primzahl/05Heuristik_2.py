def eratosthenes(n):
    zahlenliste = [z for z in range(2,n,1)]
    primezahlen = []

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


def heuristic2(n):
    dict = dict{
        n
    }
    return dict

# in einer Dictionary hineinprogrammieren
# {a:1, b:1, c:1}
# {a:2, b:2, c:1}