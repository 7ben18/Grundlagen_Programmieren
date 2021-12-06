"""
++ Bingo spiel
++ Liste mit Zahlen gegeben und mehrere Bingo Zahlen
++ Wer zuerst eine Reihe oder Zeile gefuellt hat gewinnt
++ Gesucht wird die Summe der Zeile oder Spalte sowie
++ und die Letzte Zahl, die zum Sieg fuhrte

-- Daten einlesen als Liste richtig einlesen und unterteilen in "Gezogene Zahlen" und "Bingo Feld"


"""

# Daten einlesen
with open("04testdata") as f:
    bingonums = [int(x) for x in f.readline().strip().split(",")]
    #print(bingonums) # [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

    bingofield = [x.strip().split("\n") for x in f.read().split("\n\n")]
    #print(bingofield) # [['22 13 17 11  0', ' 8  2 23  4 24', '21  9 14 16  7', ' 6 10  3 18  5', ' 1 12 20 15 19'], ['3 15  0  2 22', ' 9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4', '14 21 16 12  6'], ['14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5', ' 2  0 12  3  7']]

    bingolist = []
    for x in bingofield:
        sublist = []
        for a in x:
            sublist.append(a.split())
        bingolist.append(sublist)
    print(bingolist)

