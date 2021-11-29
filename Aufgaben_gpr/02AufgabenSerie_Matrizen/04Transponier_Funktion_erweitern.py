"""
ueberpruefen, was fuer einen Datentyp man erhalet bei Funtion flatten() und transponse()

"""
m_2d = [[1, 0, 3], [0, 2, 4]]

def transponse(n):
    if type(n) == list:
        rows = len(n)
        cols = len(n[0])

        nums = []
        for i in range(0, cols, 1):
            for s in range(0, rows, 1):
               sub = n[s][i]
               nums.append(sub)

        matrix = []
        for a in range(0,len(nums),len(n)):
            q = nums[a:a+rows]
            matrix.append(q)
        return matrix
    elif type(n) == tuple:
        # Input (2, 3, [1, 0, 3, 0, 2, 4])
        # output (3, 2, [1, 0, 0, 2, 3, 4])
        # n[0] Anzahl Zeilen 2
        # n[1] Anzahl Spalten 3
        # n[2] Matrix als Liste [1, 0, 3, 0, 2, 4]


        submatrix = []
        for i in range(0,len(n[2]),n[1]):
            submatrix.append(n[2][i:n[0]+1+i])

        rows = len(submatrix)
        cols = len(submatrix[0])

        nums = []
        for i in range(0, cols, 1):
            for s in range(0, rows, 1):
                sub = submatrix[s][i]
                nums.append(sub)

        matrix = []
        for a in range(0, len(nums), len(submatrix)):
            q = nums[a:a + rows]
            matrix.append(q)
        return matrix

        x = n[0], n[1] = n[1], n[0]
        trans = [x]

        return trans

def flatten(Matrix):
    t = []
    t.append(len(Matrix))
    t.append(len(Matrix[0]))
    #print(tuple(t))
    l = []
    for i in range(len(Matrix)):
        for y in Matrix[i]:
            l.append(y)
    t.append(l)
    return tuple(t)

#print(type(m_2d))
#print(type(flatten(m_2d)))
#print(type(m_2d) == list)
#print(type(m_2d) == tuple)

print(m_2d)
print(transponse(m_2d))
print(flatten(m_2d))
print(transponse(flatten(m_2d)))

"""
m_2d = [[1, 0, 3], [0, 2, 4]]
transpose(m_2d)
[[1, 0], [0, 2], [3, 4]]
transpose(flatten(m_2d))
(3, 2, [1, 0, 0, 2, 3, 4])
"""







