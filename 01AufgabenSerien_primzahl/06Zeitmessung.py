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

def heuristic2(n):
    thisdict = {
    }
    for i in n:
        x = 0
        for y in n:
            if y == i:
                x += 1
        thisdict[i] = x
    return thisdict



import datetime
from datetime import cnt

start = datetime.datetime.now()
print(heuristic2(distances(eratosthenes(100))))
dur = (datetime.datetime.now() - start)
time_in_seconds = (dur.microseconds + 10 ** 6 * dur.total_seconds()) / cnt / 10 ** 6

print(dur)