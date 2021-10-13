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

print(eratosthenes(100))

"""
Erster Gedankengang!

primezahlen.append(2)
for zwei in zahlenliste:
    if zwei % 2 == 0:
        zahlenliste.remove(zwei)
primezahlen.append(3)
for drei in zahlenliste:
    if drei % 3 == 0:
        zahlenliste.remove(drei)
"""

def eratosthenes2(n):
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

print(eratosthenes2(100))