"""
-- Daten einlesen
-- Addieren der einzlene Werte
--
"""

def run(dateiname):
    with open(dateiname) as f:
        return (sum([int(x) for x in f.readlines()]))

print(run("data2018_1"))

