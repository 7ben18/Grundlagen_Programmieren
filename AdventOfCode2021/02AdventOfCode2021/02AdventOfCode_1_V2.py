"""
++ forwards X = Horizontal X Schritte
++ down X = Zunahme der Tiefe
++ up X = Verringern der Tiefe
++ Start: Horizontal 0, Tiefe 0
++ Gesucht: Produkt von Position der Tiefe und Position der Horizontale

-- Daten einlesen
-- Liste erstellen fuer forwards X, down X, up X mittels if Abfrage einteilen
-- Slicing nutzen um weitere Zahlenliste zu erstellen
-- Summe aller Liste Berechnen
-- Down - up = Position der Tiefe
"""
# Einlesen der Datei
def einlesen(n):
    with open(n) as f:
        return f.read().split("\n")

def run(n):
    return sum([int(i[-1:]) for i in n if "forward" in i]) \
         * (sum([int(i[-1:]) for i in n if "down" in i]) - sum([int(i[-1:]) for i in n if "up" in i]))

print(run(einlesen("02testdata")))
print(run(einlesen("02data")))

"""
Die Aufgabe ist auch loesbar mit der library pandas
"""
