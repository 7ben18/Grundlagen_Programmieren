"""
-- Einlesen
-- o Finden (Startposition)
-- Eingabe extrahieren, konvertieren zum int
--

"""
def einlesen(data):
    with open("testdata_2019_1") as f:
        return [[str(x)] for x in f.read().split("\n")]
        #print(line)
print(einlesen("testdata_2019_1"))
