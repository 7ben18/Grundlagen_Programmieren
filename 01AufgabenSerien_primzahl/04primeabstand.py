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

"""
# Erster Gedanke, wie man die Abstaende kriegt.
    diff = []
    for a in range(0,len(primezahlen)-1,1): # Beachte die Anzahl Gesamt Elemente - 1 ! 
        x = (primezahlen[a+1] - primezahlen[a])
        x = abs(x)
        diff.append(x)
    return diff
"""

def distances(primes):
    distance = []
    for x in range(0,len(primes)-1,1):
        diff = (primes[x+1] - primes[x])
        #diff = abs(diff)
        distance.append(diff)
    return distance

print(distances(eratosthenes(100)))

def check(n):
    liste = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8]
    if liste == n:
        return True
    else:
        return False

print(check(distances(eratosthenes(100))))