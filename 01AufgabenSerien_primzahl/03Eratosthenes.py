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
    # Erstellen der Zahlenliste bis n
    zahlenliste = [z for z in range(2,n,1)]
    # Erstellen der leeren Liste fuer die Primzahlen
    primezahlen = []
    # Eine weitere liste erstellen, von zahlen bis n mit schleifen
    for i in range(2,n,1):
        # testen, ob die zahlen bis n in Zahlenliste sind
        if i in zahlenliste:
            # Wenn vorhanden, in primzahlen hinzufuegen
            primezahlen.append(i)
            # Danach auch zahl entfernen
            zahlenliste.remove(i)
        # Schleife erstellen, um die vieflachen von zahlen n zu entfernen
        for a in zahlenliste:
            # Wenn das vielfache module zahl 0 ergibt,
            if a % i == 0:
                # wird die zahl von Zahlenliste entfernt
                zahlenliste.remove(a)

    return primezahlen

print(eratosthenes2(100))