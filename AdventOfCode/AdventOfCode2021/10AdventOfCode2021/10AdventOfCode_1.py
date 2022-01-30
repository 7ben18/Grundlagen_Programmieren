"""
++ oeffnen: (, {, <, [
++ schliessen: ), }, >, ]
++ Im Datensatz, gbit es unvollstaendige und Korrupte Zeilen
++ Intressieren uns nur fuer die Korrputen Zeilen!
++ Eine Korrpute Zeile schliesst mit einem falschen Zeichen


-- Daten einlesen
"""
test = "[[<[([]))<([[{}[[()]]]"
test2 = "[[<[([]))<([[{}[[()]]]"

pairs = {"(":")",
         "[":"]",
         "{":"}",
         "<":">"}


with open("10testdata") as f:
    line = f.readline().splitlines()

    while line:
        print(line)
        line = f.readline().splitlines()