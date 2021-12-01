"""
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

7 measurements that are larger than the previous measurement
How many measurements are larger than the previous measurement?

-- Daten einlesen
-- eingelesene Daten in einer Liste speichern
-- Die zweite Zahl mit der ersten Zahl vergleichen, wenn zweite Zahl > erste Zahl + 1
-- Die dritte Zahl mit der zeiten Zahl vergleichen, wenn dritte Zahl < zweite Zahl
"""

def einlesen(data):
    with open(data) as f:
        return [int(x) for x in f.read().split("\n")]

def run(zahlenliste):
    counter = 0
    for i in range(len(zahlenliste) - 1):
        if zahlenliste[i+1] > zahlenliste[i]:
            counter += 1
    return counter

print(run(einlesen("testdata_01")))
print(run(einlesen("data_01")))
