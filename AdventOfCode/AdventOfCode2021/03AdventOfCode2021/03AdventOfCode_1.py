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
with open("03data") as f:
    line = f.read().split()
    #print(line)

    gamma = []
    epsilon = []
    liste = []
    for x in range(len(line[0])):
        for i in line:
            liste.append(i[x])

        if (liste.count("0")) > (liste.count("1")):
            gamma.append(0)
        else:
            gamma.append(1)
        liste = []

    for i in gamma:
        if i == 1:
            epsilon.append(0)
        else:
            epsilon.append(1)

    #print(gamma)
    # [1, 0, 1, 1, 0]
    #print(epsilon)
    # [0, 1, 0, 0, 1]

    gamma2 = ""
    epsilon2 = ""

    for i in gamma:
        gamma2 += str(i)

    for i in epsilon:
        epsilon2 += str(i)

    #print(gamma2)
    # 10110
    #print(epsilon2)
    # 01001

    #Umwandlung in Dezimal Zahlen
    gamma2 = int(gamma2, 2)
    epsilon2 = int(epsilon2, 2)

    #print(gamma2)
    # 22
    #print(epsilon2)
    # 9

    result = gamma2 * epsilon2
    print(result)