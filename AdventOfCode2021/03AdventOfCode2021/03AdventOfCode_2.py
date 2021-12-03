"""
++ Spaltenweise betrachten
++ Die Zahl die am meisten vorkommt notieren fuer die Spalte gibt Gamma
++ Epsilon ist das umgekehrte von Gamma
++ Gamma und Epsilon in Dezimal umrechnen und multiplizieren

-- Daten einlesen als Liste
-- Immer das X Element von jedem X Element vergleichen, counter fuer 0 und 1 erstellen
-- Mit If Abfragen 0 und 1 einteilen und Resultat in Liste appende => Gamma
-- Epsilon ist das umgekehrte von Gamma umwandeln
-- Binaere Zahlen in Dezimalzahl umwandeln
-- Produkt von Epsilon und Gamma
"""

# Date einlesen
with open("03testdata") as f:
    data = f.read().split()
    line = data


    line2 = []
    for i in range(len(line[0])):
        column = []
        for a in line:
            column.append(a[i])
        for a in line:
            if column.count("1") >= column.count("0"):
                    if a[i] == "1":
                        line2.append(a)
            elif column.count("1") < column.count("0"):
                    if a[i] == "0":
                        line2.append(a)
        line = line2
        line2 = []


    #print(line)

    O2 = line[0]
    print(O2) # oxygen generator rating

    O2 = int(O2, 2)
    print(O2)


    line = data
    #print(line)
    # ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

    for i in range(len(line[0])):
        column = []
        for a in line:
            column.append(a[i])
        for a in line:
            if column.count("1") < column.count("0"):
                    if a[i] == "1":
                        line2.append(a)
            elif column.count("1") >= column.count("0"):
                    if a[i] == "0":
                        line2.append(a)
            line = line2
            line2 = []
        if len(line) == 1:
            break

    print(line)
    CO2 = line[0]
    print(CO2)

    CO2 = int(CO2, 2)
    print(CO2)

    result = O2 * CO2
    print("Resultat ist: {}".format(result))

# Fuck off