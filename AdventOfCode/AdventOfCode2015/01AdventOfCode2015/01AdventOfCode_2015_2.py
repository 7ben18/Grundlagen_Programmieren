"""
-- Datei einlesen
-- Loops machen
-- Wahrend dem Loop checken, ob up + down einen negativen Wert aufweist.
-- Wenn neagtiven Wert - For schleife abbrechen

"""

# Datei einlesen
with open("data_2") as f:
    line = f.readline()

# Zaehlvariabel
    indexcnt = 0
    up = 0
    down = 0

    for x in line:
        if x == "(":
            up += 1
            indexcnt += 1
            if up + down < 0:
                break
        else:
            down -= 1
            indexcnt += 1
            if up + down < 0:
                break

    print(indexcnt)