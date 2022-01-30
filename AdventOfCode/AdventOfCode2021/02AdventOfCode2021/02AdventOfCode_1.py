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
with open("02data") as f:
    line = f.read().split("\n")

# Erstellen von Leeren Listen
    forwards = []
    down = []
    up = []

# Eintelung der eingelesene Datei
    for i in line:
        if "forward" in i:
            forwards.append(i)
        elif "down" in i:
            down.append(i)
        else:
            up.append(i)

# Slicing nutzen
    f = []
    d = []
    u = []
    for i in forwards:
        f.append(int(i[-1:]))

    for i in down:
        d.append(int(i[-1:]))

    for i in up:
        u.append(int(i[-1:]))

# Position der Horizontale und Tiefe berechnen
    position_horizontal = sum(f)
    position_tiefe = sum(d) - sum(u)

# Produkt von Position Horizontale und Tiefe
    result = position_tiefe * position_horizontal
    print(result)

"""
Mehrere Listen wurden erstellt, jedoch haben diese Listen keinen weiteren Nutzen nach der Verarbeitung.
Einteilung sowie Slicing in einer Schleife packen.
"""
