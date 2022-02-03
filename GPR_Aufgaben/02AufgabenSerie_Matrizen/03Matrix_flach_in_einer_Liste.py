"""
flatten([[1, 0, 3], [0, 2, 4]])
(2, 3, [1, 0, 3, 0, 2, 4])
flatten([[1, 0], [0, 2], [3, 4]])
(3, 2, [1, 0, 0, 2, 3, 4])

Ausgabe: Ein Tupple, Anzahl Zeilen, Anzahl Spalten, Zahlen in einer Liste
Anzahl Zeilen: len(Matrix)[0]
Anzahl Spalte: len(Matrix)
Zahlen der Matrix in einer liste: Leere Liste - Durch itterieren und in Liste hinzufuegen
"""

Matrix1 = [[1, 0, 3], [0, 2, 4]]
def flatten(Matrix):
    t = []
    t.append(len(Matrix))
    t.append(len(Matrix[0]))

    l = []
    for i in range(len(Matrix)):
        for y in Matrix[i]:
            l.append(y)
    t.append(l)
    return tuple(t)
print(flatten(Matrix1))
#(2, 3, [1, 0, 3, 0, 2, 4])


def flatten2(Matrix):
    return tuple([len(Matrix), len(Matrix[0]), [y for i in range(len(Matrix)) for y in Matrix[i]]])
print(Matrix1) # [[1, 0, 3], [0, 2, 4]]
print(flatten2(Matrix1)) # 2, 3, [1, 0, 3, 0, 2, 4])


