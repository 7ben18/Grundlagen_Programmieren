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

## Durch itterieren und ersertzen (Step Funktion)


# Einlesen von Daten
