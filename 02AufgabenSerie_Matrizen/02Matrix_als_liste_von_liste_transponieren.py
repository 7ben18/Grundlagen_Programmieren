"""
Programmiere eine Funktion transpose(m), die eine Matrix als Liste von Listen transponiert.
(Falls m keine wohlgeformte Matrix im Sinne von Aufgabe 1 ist,
soll ein ValueError ausgelöst werden.)
transpose([[1, 0, 3], [0, 2, 4]])
[[1, 0], [0, 2], [3, 4]]
transpose([[1, 0], [0, 2], [3, 4]])
[[1, 0, 3], [0, 2, 4]]
"""

matrix = [[1,0,3],[0,2,4]]
print(len(matrix))
print(matrix[0])

liste = []

def transponse(m):
    zeile = len(m)
    spalte = len(m[0])

    liste = []
    lenliste = len(liste)

    for x in range(len(m)):
        for i in m[x]:
            liste.append(i)


    transponsierte = []

    slicing = liste[0:2]
    transponsierte.append(slicing)

    return transponsierte

print(transponse([[1, 0, 3], [0, 2, 4]]))
print(transponse([[1, 0], [0, 2], [3, 4]]))





def transponse_shit(m):
    zeile1 = []
    zeile2 = []

    for x in m[0]:
        zeile1.append(x)

    for y in m[1]:
        zeile2.append(y)
    transponse_tuple = zip(zeile1, zeile2)
    transponse_liste = list(transponse_tuple)

    liste = []
    for x in range(len(transponse_liste)):
        liste.append(list(transponse_liste[x]))
    return liste

#print(transponse_shit([[1, 0, 3], [0, 2, 4]]))
