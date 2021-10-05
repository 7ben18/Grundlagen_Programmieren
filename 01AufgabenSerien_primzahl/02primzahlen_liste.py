"""
Aufgabe 2 – Liste der Primzahlen im Bereich 2 bis n
Die Lösung von Aufgabe 1 kann man benutzen (d.h. die Funktion is_prime aufrufen), um eine Liste aller
Primzahlen im Bereich ab 2 bis zu einer Obergrenze n zu berechnen.
"""
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n,1): # is is 2 until n
            if n % i == 0: # 4 % 2 == 0 -> 4 is not a prime!
                return False
        else:
            return True

primeliste = []
def all_primes(n):
    for i in range(2,n):
        if is_prime(i) == True:
            primeliste.append(i)

all_primes(100)
print(primeliste)

def all_primes_comprehension(n):
    return [i for i in range(2,n) if is_prime(i) == True]

print(all_primes_comprehension(100))






