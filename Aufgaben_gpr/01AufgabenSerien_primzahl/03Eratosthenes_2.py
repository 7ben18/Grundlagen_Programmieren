def eratosthenes3(n):
    zahlenliste = [i for i in range(2,n + 1,1)]
    primzahlen = []
    for s in range(2, round(n ** (1 / 2)) + 1,1):
        for i in zahlenliste:
            if i % s == 0:
                zahlenliste.remove(i)
        primzahlen.append(s)
    return zahlenliste

#print(eratosthenes3(30))
# eratosthenes Fail


