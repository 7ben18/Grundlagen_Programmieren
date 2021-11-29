"""
-- Daten einlesen als liste und integer
-- Buchstaben zaehlen, wie oft diese vorkommen
-- Anzahl der doppelten Buchstaben zusammen addieren
-- Multiplikation aus beiden Anzahlen

"""

# Daten einelsen
with open("testdata_2018_2") as f:
    line = [str(x) for x in f.readlines()]
    line = [x.strip().split() for x in line]
    print(line)


