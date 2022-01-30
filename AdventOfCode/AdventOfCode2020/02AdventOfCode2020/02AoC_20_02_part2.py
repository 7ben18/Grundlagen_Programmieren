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

#['1-3', 'a:', 'abcde']
#['1-3', 'b:', 'cdefg']
#['2-9', 'c:', 'ccccccccc']

with open("02data") as f:
    line = f.readline().strip().split()
    print(line)
    first_num = line[0]
    first_num = first_num.split("-")
    print(first_num)
    cnt = 0
    while line:
        first_num = line[0]
        first_num = first_num.split("-")
        if line[1][0] == line[2][int(first_num[0]) - 1] and line[1][0] != line[2][int(first_num[1]) - 1] \
                or line[1][0] != line[2][int(first_num[0]) - 1] and line[1][0] == line[2][int(first_num[1]) - 1]:
            cnt += 1
            first_num = []
        line = f.readline().strip().split()
    print(cnt)

