"""
1-3 a: abcde

1 = tiefere position in "Zeichenkette" (a)
3 = hoehere position in "Zeichenkette" (c)
a = Zeichen
abcde = Zeichenkette

Gesucht ist die Anzahl richtige Zeichenkette, mit der Bedingung, dass
das Zeichen entweder bei der tiefere Position oder hoehere Position
in der Zeichenkette einmal vorkommt.

1) Daten importieren
2) Elemente trennen in tiefere, hoehere, Zeichen, und Zeichenkette
3) Pruefen, tiefere, hohere Zeichen in Zeichenkette vorkommt
4) Anzahl der richtigen Zeichenkette zaehlen
"""

# 1 Daten importieren
# 4 Anzahl richtige Zeichenkette zaehlen

def valid():
    pass

def run_1():
    with open("password_testset_part2") as f:
        print(len([line for line in f if valid()]))

run_1()