# Game of Life
## Nachbar zaehlen
def num_of_neighbours(grid, row, col):
    cnt = 0
    if 0 < row and grid[row - 1][col] == '#': # Oben
        cnt += 1
    if 0 < row and 0 < col and grid[row - 1][col - 1] == '#': # Oben Links
        cnt += 1
    if 0 < row and col < len(grid) and grid[row - 1][col + 1] == '#': # Oben Rechts
        cnt += 1
    if 0 < col and grid[row][col - 1] == '#': # Links
        cnt += 1
    if col < len(grid) and grid[row][col + 1] == '#': # Rechts
        cnt += 1
    if row < len(grid) and grid[row + 1][col] == '#': # Unten
        cnt += 1
    if row < len(grid) and 0 < col and grid[row + 1][col - 1] == '#': # Unten Links
        cnt += 1
    if row < len(grid) and col < len(grid) and grid[row + 1][col + 1] == '#': # Unten Rechts
        cnt += 1
    return cnt

## Funktion funktioniert nicht
## Durch itterieren und ersertzen (Step Funktion)
def step(grid):
    new_grid = grid.copy()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            neighbours = num_of_neighbours(grid, row, col)
            if grid[row][col] == "." and neighbours == 2:
                new_grid[row][col] = "#"
            elif grid[row][col] == "#" and neighbours < 2 or neighbours > 3:
                new_grid[row][col] = "."
            else:
                new_grid[row][col] = grid[row][col]
    return new_grid



# Einlesen von Daten
## readline()

## readlines()

## strip() und split() in List Comprehension

def read_input(file_name):
    with open(file_name) as f:
        return [list(x.strip()) for x in f] #

# Main
def main():
    print(meinefunktion(parameter))

if __name__ == '__main__':
    main()

# Matrizen
## Matrix transponieren
def transponse(n):
    return [[row[i] for row in n] for i in range(len(n[0]))]
print(transponse([[1, 0, 3], [0, 2, 4]]))
# [[1, 0], [0, 2], [3, 4]]

## Matrix flatten
Matrix1 = [[1, 0, 3], [0, 2, 4]]
def flatten(Matrix):
    t = []
    t.append(len(Matrix))
    t.append(len(Matrix[0]))
    l = [[y for y in Matrix[i]] for i in range(len(Matrix))]
    #for i in range(len(Matrix)):
    #    for y in Matrix[i]:
    #        l.append(y)
    t.append(l)
    return tuple(t)
print(flatten(Matrix1))
#(2, 3, [1, 0, 3, 0, 2, 4])

# Primzahlen
## Primzahl True oder False?
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(5)) # True
print(is_prime(8)) # False

## Liste von Primzahlen
def all_primes_comprehension(n):
    return [i for i in range(2,n) if is_prime(i)]
print(all_primes_comprehension(10)) # [2, 3, 5, 7]

# List comprehension
## Summe von einer Liste
lst1 = sum((x for x in range(10)))
print(lst1)
## Liste
lst2 = [x for x in range(10)]
print(lst2)
# Objekt
lst3 = ((2 * x for x in range(10)))
print(lst3)
# Tupple
lst4 = tuple((2 * x for x in range(10)))
print(lst4)
# set
lst5 = set((2 * x for x in range(10)))
print(lst5)
# Dictionary
lst6 = {x * 2: x for x in range(10)}
print(lst6)
# Addition Subtraktion Multiplikation Division von Listen
def add(n):
    return n + 10
lst7 = [add(x) for x in range(10)]
print(lst7)

# Haeufigkeit von Zahlen in einer Liste
lst = [1,1,1,3,4,5,6]
def heuristic(n):
    thisdict = {
    }
    for i in n:
        x = 0
        for y in n:
            if y == i:
                x += 1
        thisdict[i] = x
    return thisdict
print(heuristic(lst))
#{1: 3, 3: 1, 4: 1, 5: 1, 6: 1}