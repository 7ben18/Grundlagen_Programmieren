"""
-- Daten einelsen
-- If else Schleife mit Floorup, Floordown
-- Floorup = (
-- Floordown = (
-- Summe Bilden = Floorlevel

"""

# Daten einlesen
with open("testdata_1") as f:
    line = f.readline()
    print(line)

# Zaehlvariabel definieren
    floorup = 0
    floordown = 0

# Foor Loop erstellen mit Bedingungen
    for i in line:
        if i == "(":
            floorup += 1
        else:
            floordown -= 1

# Resultate ausgeben
    print(floorup, floordown)
    print(floorup + floordown)

# Als Funktion:
def run(datei):
    with open(datei) as f:
        line = f.readline()

        floorup = 0
        floordown = 0

        for i in line:
            if i == "(":
                floorup += 1
            else:
                floordown -= 1

    return floorup + floordown

print(run("data_1"))