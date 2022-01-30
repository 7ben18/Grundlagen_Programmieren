"""
++ down X Zunahme von aim bei X Einheiten
++ up X Verringern von aim bei X Einheiten
++ forwards X macht zwei Sachen:
++ 1) forwards X Fuegt Horzontale Position bei X Einheiten
++ 2) forwards X macht aim * X = Position der Tiefe
++ aim und Horizontale Position und Tiefe startet bei 0

-- Datei einlesen Zeilen fuer Zeile betrachtet

"""

# Datei einlesen
with open("02data") as f:
    line = f.readline().split()

    horizontal = 0
    depth = 0
    aim = 0

    while line:
        if line[0] == "forward":
            horizontal += int(line[1])
            depth += int(line[1]) * aim
        if line[0] == "down":
            aim += int(line[1])
        if line[0] == "up":
            aim -= int(line[1])
        line = f.readline().split()

    print(horizontal * depth)
