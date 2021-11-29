"""
Aufgabe 1 – Einfacher Primzahltest
Eine Primzahl ist eine natürliche Zahl grösser als 1, die durch keine andere natürliche Zahl teilbar ist,
ausser 1 und sich selbst.
Um zu testen, ob eine ganze Zahl n ≥ 2 eine Primzahl ist, kann man für alle grundsätzlich geeigneten
ganzen Zahlen t prüfen, ob t die Zahl n ganzzahlig teilt – d.h. es gibt eine ganze Zahl s so dass s · t = n –
und aus dem Fund oder Nicht-Fund geeignete Schlüsse ziehen.
Schreibe eine Python-Funktion is_prime(n) auf, die einen entsprechenden Wahrheitswert zurückgibt:
is_prime(1)
False
is_prime(2)
True
is_prime(3)
True
is_prime(4)
False
is_
"""


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if (n % i) == 0:  # 4 % 2 == 0 -> 4 is not a prime!
                return False
            return True


print(is_prime(10))
print(is_prime(17))


def is_prime2(n):
    if n < 1:
        return False
    if n > 2:
        for i in range(2, n // 2 + 1, 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def is_prime3(n):
    if n % 2 == 0:
        return n == 2
    i = 3
    while i <= n / 2 and n % i != 0:
        i = i + 1
    return not (i <= n / 2)


for x in range(2, 10):
    print(x, "prime?", is_prime3(x))


def is_prime4(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

for x in range(2,10):
    if is_prime4(x): print(x)
