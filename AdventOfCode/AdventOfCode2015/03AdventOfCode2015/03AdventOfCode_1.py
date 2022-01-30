"""
++ north (^), south (v), east (>), or west (<)
++ >  2 Haeuser erhalten Geschenke (Starthaus und Easthaus)
++ ^>v< , 4 Haeuser erhalten Geschenke  Nordhaus, Nordhaus und Easthaus, Southhaus, westhaust
++  ^v^v^v^v^v 2 Haeuser erhalten Geschenke, Nordhaus und Southhaus

"""

def einlesen(daten):
    with open(daten) as f:
        return [x for x in f.readline()]

testdaten = einlesen("03testdata")
daten = einlesen("03data")

def present(i):
    if i == ">":
        return 2
    if i == "<":
        return 1
    if i == "v":
        return 1
    if i == "^":
        return 1
    else:
        return 0
