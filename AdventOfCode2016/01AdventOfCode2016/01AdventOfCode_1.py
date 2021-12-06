"""
-- North East South West
-- faced North
-- L - Left turn 90, R - Right turn
-- Blocks away?

-- Daten einelsen
-- X und Y Counter
"""

# Einlesen
def einlesen(daten):
    with open(daten) as f:
        line = [x.strip() for x in f.readline().split(",")]
        return line

data = einlesen("01data")
testdata = einlesen("01testdata")

x_cor = 0
y_cor = 0

for i in testdata:
    if i[0:1] == "R":
        x_cor += int(i[-1:])
    else:
        y_cor += int(i[-1:])
