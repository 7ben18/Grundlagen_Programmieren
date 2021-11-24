"""
as_dict([[1, 0, 3], [0, 2, 4]])
(2, 3, {(0, 0): 1, (0, 2): 3, (1, 1): 2, (1, 2): 4})
as_dict([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
(4, 4, {})
as_dict([[5]])
(1, 1, {(0, 0): 5})

output: in einem tupple,
Anzahl Zeilen
Anzahl Spalten
Dictonary
"""

matrix = [[1, 0, 3], [0, 2, 4]]

def as_dict(matrix):
    zeilen = len(matrix)
    spalten = len(matrix[0])

    thisdict = {}
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if matrix[i][k] != 0:
              thisdict[i,k] = matrix[i][k]
    return (zeilen, spalten, thisdict)
print(as_dict(matrix))

def as_dict2(matrix):

    return (len(matrix), len(matrix[0]), {(i,k):matrix[i][k] for i in range(len(matrix)) for k in range(len(matrix[i])) \
            if matrix[i][k] != 0})
print(as_dict2(matrix))