"""
Programmiere eine Funktion well_formed_matrix(m), welche die genannten Eigenschaften prüft:
well_formed_matrix([])
False
well_formed_matrix([[], []])
False
well_formed_matrix([[1], [1,2]])
False
well_formed_matrix([[0,0], [1,2]])
True
"""

def well_formed_matrix(n):
    # checken, ob Anzahl der Zeilen < 2 ist.
    if len(n) < 2:
        return False

    # Anzahl Zeilen
    rows = len(n)

    # checken, ob Anzahl der Zeilen gleich der Anzahl Spalten entspricht
    for i in range(0,rows):
        if rows != len(n[i]):
            return False
        else:
            return True

print(well_formed_matrix([]))
print(well_formed_matrix([[], []]))
print(well_formed_matrix([[1], [1,2]]))
print(well_formed_matrix([[0,0], [1,2]]))