"""
Programmiere eine Funktion transpose(m), die eine Matrix als Liste von Listen transponiert.
(Falls m keine wohlgeformte Matrix im Sinne von Aufgabe 1 ist,
soll ein ValueError ausgelöst werden.)
transpose([[1, 0, 3], [0, 2, 4]])
[[1, 0], [0, 2], [3, 4]]
transpose([[1, 0], [0, 2], [3, 4]])
[[1, 0, 3], [0, 2, 4]]
"""

def transponse(n):
    rows = len(n)
    cols = len(n[0])

    nums = []
    for i in range(0, cols, 1):
        for s in range(0, rows, 1):
           sub = n[s][i]
           nums.append(sub)

    matrix = []
    for a in range(0,cols,1):
        q = nums[a:a+rows]
        matrix.append(q)
    return matrix

print(transponse([[1, 0, 3], [0, 2, 4]]))
print(transponse([[1, 0], [0, 2], [3, 4]]))