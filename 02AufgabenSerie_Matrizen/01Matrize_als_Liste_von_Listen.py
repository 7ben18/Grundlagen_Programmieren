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

matrix = [[1,0,3],[1,2,1]]
print(len(matrix))
print(len(matrix[0]))
print(len(matrix[1]))

def well_formed_matrix(m):
    if not(len(m) < 1 or len(m[0]) != len(m[1]) or len(m[0]) < 1):
        return False
    else:
        return True

print(well_formed_matrix([]))
print(well_formed_matrix([[], []]))
print(well_formed_matrix([[1], [1,2]]))
print(well_formed_matrix([[0,0], [1,2]]))








