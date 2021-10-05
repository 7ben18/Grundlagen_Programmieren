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
        for i in range(2,n):
            if (n % i) == 0: # 4 % 2 == 0 -> 4 is not a prime!
                return False
        else:
            return True

print(is_prime(15))
print(is_prime(21))
print(is_prime(30))
print(is_prime(17))