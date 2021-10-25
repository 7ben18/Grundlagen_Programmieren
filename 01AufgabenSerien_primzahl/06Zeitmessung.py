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



import time
start1 = time.perf_counter()
print(heuristic2(distances(eratosthenes(1000))))
end1 = time.perf_counter()
zeit1 = end1 - start1
print(zeit1) # output in sekunde

import datetime
start2 = datetime.datetime.now()
print(heuristic2(distances(eratosthenes(1000))))
dur = (datetime.datetime.now() - start2)
print(dur)