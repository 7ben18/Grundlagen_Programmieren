"""
-- Daten einlesen als liste und integer
-- Buchstaben zaehlen, wie oft diese vorkommen
-- Anzahl der doppelten Buchstaben zusammen addieren
-- Multiplikation aus beiden Anzahlen

"""

# Daten einelsen
with open("testdata_2018_2") as f:
    line = [str(x) for x in f.readlines()]
    line = [x.strip() for x in line]
    print(line)

    masterdict = {}


    for i in range(len(line)):
        dict = {}
        cnt = 1
        masterdict[i] = dict

        for a in line[i]:
            if a in dict:
                cnt += 1
                dict[a] = cnt
            else:
                dict[a] = cnt

    print(masterdict)
